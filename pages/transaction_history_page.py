from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.env import BASE_URL

class TransactionHistoryPage(BasePage):

    # Selector
    new_transaction_button = (By.CSS_SELECTOR, '[data-testid="transaction-new-button"]')

    table = (By.CSS_SELECTOR, '[data-testid="transaction-table"]')
    rows = (By.CSS_SELECTOR, '[data-testid="transaction-row"]')

    month_filter = (By.CSS_SELECTOR, '[data-testid="transaction-filter-month"]')
    year_filter = (By.CSS_SELECTOR, '[data-testid="transaction-filter-year"]')
    filter_submit = (By.CSS_SELECTOR, '[data-testid="transaction-filter-submit"]')

    detail_buttons = (By.CSS_SELECTOR, '[data-testid="transaction-detail-button"]')
    receipt_buttons = (By.CSS_SELECTOR, '[data-testid="transaction-receipt-button"]')

    report_download_button = (By.CSS_SELECTOR, '[data-testid="transaction-download-report"]')

    # Action
    def open(self):
        self.open_url(f"{BASE_URL}/transactions")
        self.is_visible(self.table)

    def filter_by_month_year(self, month, year):
        table = self.find(self.table)

        Select(self.find(self.month_filter)).select_by_value(str(month))
        Select(self.find(self.year_filter)).select_by_value(str(year))
        self.click(self.filter_submit)

        self.wait.until(EC.staleness_of(table))

        self.is_visible(self.table)

    def click_new_transaction(self):
        self.click(self.new_transaction_button)

    def open_first_detail(self):
        self.find_all(self.detail_buttons)[0].click()

    def open_first_receipt(self):
        self.find_all(self.receipt_buttons)[0].click()

    # Helpers
    def count(self):
        return len(self.find_all(self.rows))

    def get_report_download_url(self):
        return self.find(self.report_download_button).get_attribute("href")

    def current_url(self):
        return self.driver.current_url