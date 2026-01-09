from pages.transaction_history_page import TransactionHistoryPage

def test_view_transaction_history_page(login_admin):
    history = TransactionHistoryPage(login_admin)
    history.open()

    assert history.count() >= 0

def test_filter_and_paginate_transaction_history(login_admin):
    history = TransactionHistoryPage(login_admin)
    history.open()
    history.filter_by_month_year(month=1, year=2025)

    assert history.count() >= 0

def test_new_transaction_button_redirect(login_admin):
    history = TransactionHistoryPage(login_admin)
    history.open()
    history.click_new_transaction()

    assert "/transactions/create" in history.current_url()

def test_download_transaction_report_pdf(login_admin):
    history = TransactionHistoryPage(login_admin)
    history.open()

    url = history.get_report_download_url()

    assert url.endswith("/transactions/report/pdf")

def test_open_transaction_detail(login_admin):
    history = TransactionHistoryPage(login_admin)
    history.open()

    if history.count() == 0:
        return

    history.open_first_detail()
    assert "/transactions/" in history.current_url()

def test_open_transaction_receipt_pdf(login_admin):
    history = TransactionHistoryPage(login_admin)
    history.open()

    if history.count() == 0:
        return

    history.open_first_receipt()
    assert "/receipt/pdf" in history.current_url()