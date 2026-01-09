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

from pages.product_page import ProductPage

def test_admin_can_view_product_page(login_admin):
    product = ProductPage(login_admin)
    product.open()

    assert product.count() >= 0

def test_admin_can_create_product(login_admin):
    product = ProductPage(login_admin)
    product.open()
    product.open_create_form()
    product.create(category="Makanan",
        name="Produk Selenium",
        price="15000",
        image_path="assets/images/image.jpg"
        )

    assert "berhasil" in product.get_success_message()

def test_admin_can_edit_product(login_admin):
    product = ProductPage(login_admin)
    product.open()
    product.open_first_edit()
    product.update_name("Produk Updated")

    assert "berhasil" in product.get_success_message()

def test_admin_can_delete_product(login_admin):
    product = ProductPage(login_admin)
    product.open()
    before = product.count()

    product.delete_first()
    product.open()

    after = product.count()
    assert after <= before
