from pages.login_page import LoginPage
from pages.transaction_page import TransactionPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD


def test_admin_can_open_transaction_page(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    transaction = TransactionPage(driver)
    transaction.open_create()

    assert "/transactions/create" in transaction.get_current_url()


def test_admin_can_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    transaction = TransactionPage(driver)
    transaction.open_create()
    transaction.add_first_product_to_cart()

    assert not transaction.is_cart_empty()


def test_admin_can_create_transaction_with_cash(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    transaction = TransactionPage(driver)
    transaction.open_create()

    transaction.add_first_product_to_cart()
    transaction.select_cash_payment()
    transaction.submit_transaction()

    # redirect ke detail transaksi
    assert "/transactions/" in transaction.get_current_url()


def test_admin_can_create_transaction_with_qris(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    transaction = TransactionPage(driver)
    transaction.open_create()

    transaction.add_first_product_to_cart()
    transaction.select_qris_payment()
    transaction.submit_transaction()
    transaction.confirm_qris_payment()

    assert "/transactions/" in transaction.get_current_url()
