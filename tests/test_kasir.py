from pages.kasir_page import KasirPage

def test_admin_can_view_kasir_page(login_admin):
    kasir = KasirPage(login_admin)
    kasir.open()

    assert kasir.count() >= 0

def test_admin_can_create_kasir(login_admin):
    kasir = KasirPage(login_admin)
    kasir.open()
    kasir.open_create_form()
    kasir.create("Kasir Selenium", "kasir_selenium@test.com")

    assert "berhasil" in kasir.get_success_message()

def test_admin_can_edit_kasir(login_admin):
    kasir = KasirPage(login_admin)
    kasir.open()
    kasir.open_first_edit()
    kasir.update_name("Kasir Updated")

    assert "berhasil" in kasir.get_success_message()

def test_admin_can_delete_kasir(login_admin):
    kasir = KasirPage(login_admin)
    kasir.open()
    before = kasir.count()

    kasir.delete_first()
    kasir.open()

    after = kasir.count()
    assert after <= before
