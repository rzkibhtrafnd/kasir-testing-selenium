from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.env import BASE_URL

class KasirPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selector
    add_button = (By.CSS_SELECTOR, '[data-testid="add-kasir-button"]')
    table = (By.CSS_SELECTOR, '[data-testid="kasir-table"]')
    rows = (By.CSS_SELECTOR, '[data-testid="kasir-row"]')

    name_input = (By.CSS_SELECTOR, '[data-testid="kasir-name-input"]')
    email_input = (By.CSS_SELECTOR, '[data-testid="kasir-email-input"]')
    submit_button = (By.CSS_SELECTOR, '[data-testid="submit-kasir-button"]')

    edit_buttons = (By.CSS_SELECTOR, '[data-testid="edit-kasir-button"]')
    delete_buttons = (By.CSS_SELECTOR, '[data-testid="delete-kasir-button"]')

    success_message = (By.CSS_SELECTOR, '[data-testid="alert-success"]')

    # Action
    def open(self):
        self.open_url(f"{BASE_URL}/admin/kasir")
        self.is_visible(self.table)

    def open_create_form(self):
        self.click(self.add_button)

    def create(self, name, email):
        self.find(self.name_input).send_keys(name)
        self.find(self.email_input).send_keys(email)
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