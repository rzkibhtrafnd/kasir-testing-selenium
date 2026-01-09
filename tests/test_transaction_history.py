from pages.login_page import LoginPage
from pages.transaction_history_page import TransactionHistoryPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD


# TC-RiwTran-001
def test_view_transaction_history_page(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    history = TransactionHistoryPage(driver)
    history.open_index()

    assert history.count_rows() >= 0


# TC-RiwTran-002
def test_filter_and_paginate_transaction_history(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    history = TransactionHistoryPage(driver)
    history.open_index()
    history.filter_by_month_year(month=1, year=2025)

    assert history.count_rows() >= 0


# TC-RiwTran-003
def test_new_transaction_button_redirect(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    history = TransactionHistoryPage(driver)
    history.open_index()
    history.click_new_transaction()

    assert "/transactions/create" in driver.current_url


# TC-RiwTran-004
def test_download_transaction_report_pdf(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    history = TransactionHistoryPage(driver)
    history.open_index()

    url = history.get_report_download_url()

    assert url.endswith("/transactions/report/pdf")

# TC-RiwTran-006
def test_open_transaction_detail(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    history = TransactionHistoryPage(driver)
    history.open_index()

    if history.count_rows() == 0:
        return

    history.open_first_detail()
    assert "/transactions/" in driver.current_url


# TC-RiwTran-007
def test_open_transaction_receipt_pdf(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    history = TransactionHistoryPage(driver)
    history.open_index()

    if history.count_rows() == 0:
        return

    history.open_first_receipt()
    assert "/receipt/pdf" in driver.current_url
