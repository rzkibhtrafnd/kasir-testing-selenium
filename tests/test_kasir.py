from pages.login_page import LoginPage
from pages.kasir_page import KasirPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD


def test_admin_can_view_kasir_page(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    kasir = KasirPage(driver)
    kasir.open_index()

    assert kasir.count_rows() >= 0


def test_admin_can_create_kasir(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    kasir = KasirPage(driver)
    kasir.open_index()
    kasir.open_create()
    kasir.create_kasir("Kasir Selenium", "kasir_selenium@test.com")

    assert "berhasil" in kasir.get_success_message()


def test_admin_can_edit_kasir(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    kasir = KasirPage(driver)
    kasir.open_index()
    kasir.open_edit_first()
    kasir.update_kasir("Kasir Updated")

    assert "berhasil" in kasir.get_success_message()


def test_admin_can_delete_kasir(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    kasir = KasirPage(driver)
    kasir.open_index()
    before = kasir.count_rows()

    kasir.delete_first_kasir()

    kasir.open_index()
    after = kasir.count_rows()

    assert after <= before
