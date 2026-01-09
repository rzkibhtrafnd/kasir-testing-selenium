from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD

def test_admin_can_view_product_page(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    product = ProductPage(driver)
    product.open_index()

    assert product.count_rows() >= 0


def test_admin_can_create_product(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    product = ProductPage(driver)
    product.open_index()
    product.open_create()
    product.create_product(
        category="Makanan",
        name="Produk Selenium",
        price="15000",
        image_path="assets/images/image.jpg"
        )

    assert "berhasil" in product.get_success_message()


def test_admin_can_edit_product(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    product = ProductPage(driver)
    product.open_index()
    product.open_edit_first()
    product.update_product("product Updated")

    assert "berhasil" in product.get_success_message()


def test_admin_can_delete_product(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    product = ProductPage(driver)
    product.open_index()
    before = product.count_rows()

    product.delete_first_product()

    product.open_index()
    after = product.count_rows()

    assert after <= before
