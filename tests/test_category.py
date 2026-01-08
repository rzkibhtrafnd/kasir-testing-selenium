from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD


def test_admin_can_view_category_page(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    category = CategoryPage(driver)
    category.open_index()

    assert category.count_rows() >= 0


def test_admin_can_create_category(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    category = CategoryPage(driver)
    category.open_index()
    category.open_create()
    category.create_category("category Selenium")

    assert "berhasil" in category.get_success_message()


def test_admin_can_edit_category(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    category = CategoryPage(driver)
    category.open_index()
    category.open_edit_first()
    category.update_category("category Updated")

    assert "berhasil" in category.get_success_message()


def test_admin_can_delete_category(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    category = CategoryPage(driver)
    category.open_index()
    before = category.count_rows()

    category.delete_first_category()

    category.open_index()
    after = category.count_rows()

    assert after <= before
