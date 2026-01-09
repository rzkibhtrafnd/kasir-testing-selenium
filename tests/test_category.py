from pages.category_page import CategoryPage

def test_admin_can_view_category_page(login_admin):
    category = CategoryPage(login_admin)
    category.open()

    assert category.count() >= 0

def test_admin_can_create_category(login_admin):
    category = CategoryPage(login_admin)
    category.open()
    category.open_create_form()
    category.create("Category Selenium")

    assert "berhasil" in category.get_success_message()

def test_admin_can_edit_category(login_admin):
    category = CategoryPage(login_admin)
    category.open()
    category.open_first_edit()
    category.update_name("Category Updated")

    assert "berhasil" in category.get_success_message()

def test_admin_can_delete_category(login_admin):
    category = CategoryPage(login_admin)
    category.open()
    before = category.count()

    category.delete_first()
    category.open()

    after = category.count()
    assert after <= before
