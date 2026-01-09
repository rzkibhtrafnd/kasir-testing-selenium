import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from config.env import BASE_URL

class ProductPage(BasePage):

    # Selector
    add_button = (By.CSS_SELECTOR, '[data-testid="add-product-button"]')
    table = (By.CSS_SELECTOR, '[data-testid="product-table"]')
    rows = (By.CSS_SELECTOR, '[data-testid="product-row"]')

    category_select = (By.CSS_SELECTOR, '[data-testid="category-select"]')
    name_input = (By.CSS_SELECTOR, '[data-testid="product-name-input"]')
    image_input = (By.CSS_SELECTOR, '[data-testid="product-image-input"]')
    price_input = (By.CSS_SELECTOR, '[data-testid="product-price-input"]')
    submit_button = (By.CSS_SELECTOR, '[data-testid="submit-product-button"]')

    edit_buttons = (By.CSS_SELECTOR, '[data-testid="edit-product-button"]')
    delete_buttons = (By.CSS_SELECTOR, '[data-testid="delete-product-button"]')

    success_message = (By.CSS_SELECTOR, '[data-testid="alert-success"]')

    # Actions
    def open(self):
        self.driver.get(f"{BASE_URL}/admin/products")
        self.is_visible(self.table)

    def open_create_form(self):
        self.click(self.add_button)

    def create(self, category, name, price, image_path):
        select = Select(self.find(self.category_select))
        select.select_by_visible_text(category)

        self.find(self.name_input).send_keys(name)
        self.find(self.price_input).send_keys(price)

        abs_path = os.path.abspath(image_path)
        self.find(self.image_input).send_keys(abs_path)

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