from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.env import BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== SELECTORS =====
    email = (By.CSS_SELECTOR, '[data-testid="email-input"]')
    password = (By.CSS_SELECTOR, '[data-testid="password-input"]')
    login_button = (By.CSS_SELECTOR, '[data-testid="login-button"]')

    user_menu_button = (By.CSS_SELECTOR, '[data-testid="user-menu-button"]')
    logout_button = (By.CSS_SELECTOR, '[data-testid="logout-button"]')

    error_message = (By.CSS_SELECTOR, '.text-red-600')
    success_message = (By.CSS_SELECTOR, '.text-green-600')

    # ===== ACTIONS =====
    def open_login(self):
        self.driver.get(f"{BASE_URL}/login")

    def login(self, email, password):
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.email)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.driver.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(*self.login_button).click()

        self.wait.until(
            lambda d: d.current_url != f"{BASE_URL}/login"
            or self.get_error_message()
        )

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.user_menu_button)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

        self.wait.until(EC.url_contains("/login"))

    # ===== HELPERS =====
    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_message).text.strip()
        except:
            return ""

    def get_success_message(self):
        try:
            return self.driver.find_element(*self.success_message).text.strip()
        except:
            return ""

