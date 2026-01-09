from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.env import BASE_URL

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selector
    email_input = (By.CSS_SELECTOR, '[data-testid="email-input"]')
    password_input = (By.CSS_SELECTOR, '[data-testid="password-input"]')
    login_button = (By.CSS_SELECTOR, '[data-testid="login-button"]')

    user_menu_button = (By.CSS_SELECTOR, '[data-testid="user-menu-button"]')
    logout_button = (By.CSS_SELECTOR, '[data-testid="logout-button"]')

    error_message = (By.CSS_SELECTOR, '.text-red-600')
    success_message = (By.CSS_SELECTOR, '.text-green-600')

    # Action
    def open(self):
        self.driver.get(f"{BASE_URL}/login")

    def login(self, email, password):
        self.find(self.email_input).clear()
        self.find(self.email_input).send_keys(email)

        self.find(self.password_input).clear()
        self.find(self.password_input).send_keys(password)

        self.click(self.login_button)

        # Tunggu redirect atau error muncul
        self.wait.until(
            lambda d: "/login" not in d.current_url or self.has_error()
        )

    def logout(self):
        self.click(self.user_menu_button)
        self.click(self.logout_button)
        self.wait.until(lambda d: "/login" in d.current_url)

    # Helpers
    def has_error(self):
        return bool(self.get_error_message())

    def get_error_message(self):
        elements = self.driver.find_elements(*self.error_message)
        return elements[0].text.strip() if elements else ""

    def get_success_message(self):
        elements = self.driver.find_elements(*self.success_message)
        return elements[0].text.strip() if elements else ""

