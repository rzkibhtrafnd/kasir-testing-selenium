from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.env import BASE_URL

class TransactionPage(BasePage):

    # Selector
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

    # Actions
    def open(self):
        self.open_url(f"{BASE_URL}/transactions/create")
        self.find_all(self.product_cards)

    def add_product(self, index=0):
        self.find_all(self.add_to_cart_buttons)[index].click()

    def select_cash_payment(self):
        self.click(self.cash_radio)

    def select_qris_payment(self):
        self.click(self.qris_radio)

    def submit(self):
        self.click(self.submit_button)

    def confirm_qris(self):
        self.is_visible(self.qris_modal)
        self.click(self.qris_confirm)

    # Helpers
    def is_cart_empty(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, "#cartItems > div")
        return len(items) == 0

    def current_url(self):
        return self.driver.current_url
