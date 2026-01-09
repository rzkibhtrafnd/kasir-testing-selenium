from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.env import BASE_URL


class CategoryPage(BasePage):

    # Selector
    add_button = (By.CSS_SELECTOR, '[data-testid="add-category-button"]')
    table = (By.CSS_SELECTOR, '[data-testid="category-table"]')
    rows = (By.CSS_SELECTOR, '[data-testid="category-row"]')

    name_input = (By.CSS_SELECTOR, '[data-testid="category-name-input"]')
    submit_button = (By.CSS_SELECTOR, '[data-testid="submit-category-button"]')

    edit_buttons = (By.CSS_SELECTOR, '[data-testid="edit-category-button"]')
    delete_buttons = (By.CSS_SELECTOR, '[data-testid="delete-category-button"]')

    success_message = (By.CSS_SELECTOR, '[data-testid="alert-success"]')

    # Actions
    def open(self):
        self.open_url(f"{BASE_URL}/admin/categories")
        self.is_visible(self.table)

    def open_create_form(self):
        self.click(self.add_button)

    def create(self, name):
        self.find(self.name_input).send_keys(name)
        self.click(self.submit_button)

    def open_first_edit(self):
        self.find_all(self.edit_buttons)[0].click()

    def update_name(self, name):
        field = self.find(self.name_input)
        field.clear()
        field.send_keys(name)
        self.click(self.submit_button)

    def delete_first(self):
        self.find_all(self.delete_buttons)[0].click()
        self.driver.switch_to.alert.accept()

    # Helpers
    def count(self):
        return len(self.find_all(self.rows))

    def get_success_message(self):
        elements = self.driver.find_elements(*self.success_message)
        return elements[0].text.lower() if elements else ""