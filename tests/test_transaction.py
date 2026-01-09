from pages.transaction_page import TransactionPage

def test_admin_can_open_transaction_page(login_admin):
    transaction = TransactionPage(login_admin)
    transaction.open()

    assert "/transactions/create" in transaction.current_url()

def test_admin_can_add_product_to_cart(login_admin):
    transaction = TransactionPage(login_admin)
    transaction.open()
    transaction.add_product()

    assert not transaction.is_cart_empty()

def test_admin_can_create_transaction_with_cash(login_admin):
    transaction = TransactionPage(login_admin)
    transaction.open()

    transaction.add_product()
    transaction.select_cash_payment()
    transaction.submit()

    assert "/transactions/" in transaction.current_url()

def test_admin_can_create_transaction_with_qris(login_admin):
    transaction = TransactionPage(login_admin)
    transaction.open()

    transaction.add_product()
    transaction.select_qris_payment()
    transaction.submit()
    transaction.confirm_qris()

    assert "/transactions/" in transaction.current_url()
