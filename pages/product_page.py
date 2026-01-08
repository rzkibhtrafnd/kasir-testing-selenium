import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.env import BASE_URL

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #selector
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

    #actions
    def open_index(self):
        self.driver.get(f"{BASE_URL}/admin/products")
        self.wait.until(EC.visibility_of_element_located(self.table))

    def open_create(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    def select_category_by_text(self, category_name):
        select_el = self.wait.until(
            EC.visibility_of_element_located(self.category_select)
        )
        Select(select_el).select_by_visible_text(category_name)

    def create_product(self, category, name, price, image_path):
        self.select_category_by_text(category)

        self.wait.until(
            EC.visibility_of_element_located(self.name_input)
        ).send_keys(name)

        self.driver.find_element(*self.price_input).send_keys(price)

        abs_path = os.path.abspath(image_path)
        self.driver.find_element(*self.image_input).send_keys(abs_path)

        self.driver.find_element(*self.submit_button).click()

    def open_edit_first(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.edit_buttons)
        )
        buttons[0].click()

    def update_product(self, name):
        field = self.wait.until(EC.visibility_of_element_located(self.name_input))
        field.clear()
        field.send_keys(name)
        self.driver.find_element(*self.submit_button).click()

    def delete_first_product(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.delete_buttons)
        )
        buttons[0].click()

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).text

    def count_rows(self):
        return len(self.driver.find_elements(*self.rows))