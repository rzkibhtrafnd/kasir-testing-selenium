from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.env import BASE_URL
import json
import time

class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #selector
    product_cards = (By.CSS_SELECTOR, '.product-card')
    add_to_cart_buttons = (By.CSS_SELECTOR, '.add-to-cart-btn')

    cart_items = (By.ID, 'cartItems')
    empty_cart = (By.ID, 'emptyCart')
    submit_button = (By.ID, 'submitBtn')
    clear_cart_button = (By.ID, 'clearCartBtn')

    cart_input = (By.ID, 'cartInput')

    cash_radio = (By.CSS_SELECTOR, 'input[name="payment_method"][value="cash"]')
    qris_radio = (By.CSS_SELECTOR, 'input[name="payment_method"][value="qris"]')

    qris_modal = (By.ID, 'qrisModal')
    qris_confirm = (By.ID, 'confirmQris')

    #actions
    def open_create(self):
        self.driver.get(f"{BASE_URL}/transactions/create")
        self.wait.until(EC.presence_of_element_located(self.product_cards))

    def add_first_product_to_cart(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.add_to_cart_buttons)
        )
        buttons[0].click()

    def add_product_by_index(self, index=0):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.add_to_cart_buttons)
        )
        buttons[index].click()

    def select_cash_payment(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cash_radio)
        ).click()

    def select_qris_payment(self):
        self.wait.until(
            EC.element_to_be_clickable(self.qris_radio)
        ).click()

    def submit_transaction(self):
        self.wait.until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()

    def confirm_qris_payment(self):
        self.wait.until(
            EC.visibility_of_element_located(self.qris_modal)
        )
        self.wait.until(
            EC.element_to_be_clickable(self.qris_confirm)
        ).click()

    def is_cart_empty(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, "#cartItems > div")
        return len(items) == 0

    def clear_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.clear_cart_button)
        ).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def get_current_url(self):
        return self.driver.current_url
