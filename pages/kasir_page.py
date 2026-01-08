from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.env import BASE_URL

class KasirPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== SELECTORS =====
    add_button = (By.CSS_SELECTOR, '[data-testid="add-kasir-button"]')
    table = (By.CSS_SELECTOR, '[data-testid="kasir-table"]')
    rows = (By.CSS_SELECTOR, '[data-testid="kasir-row"]')

    name_input = (By.CSS_SELECTOR, '[data-testid="kasir-name-input"]')
    email_input = (By.CSS_SELECTOR, '[data-testid="kasir-email-input"]')
    submit_button = (By.CSS_SELECTOR, '[data-testid="submit-kasir-button"]')

    edit_buttons = (By.CSS_SELECTOR, '[data-testid="edit-kasir-button"]')
    delete_buttons = (By.CSS_SELECTOR, '[data-testid="delete-kasir-button"]')

    success_message = (By.CSS_SELECTOR, '[data-testid="alert-success"]')

    # ===== ACTIONS =====
    def open_index(self):
        self.driver.get(f"{BASE_URL}/admin/kasir")
        self.wait.until(EC.visibility_of_element_located(self.table))

    def open_create(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    def create_kasir(self, name, email):
        self.wait.until(EC.visibility_of_element_located(self.name_input)).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.submit_button).click()

    def open_edit_first(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.edit_buttons)
        )
        buttons[0].click()

    def update_kasir(self, name):
        field = self.wait.until(EC.visibility_of_element_located(self.name_input))
        field.clear()
        field.send_keys(name)
        self.driver.find_element(*self.submit_button).click()

    def delete_first_kasir(self):
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
