from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.env import BASE_URL

class TransactionHistoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #selector
    new_transaction_button = (By.CSS_SELECTOR, '[data-testid="transaction-new-button"]')

    table = (By.CSS_SELECTOR, '[data-testid="transaction-table"]')
    rows = (By.CSS_SELECTOR, '[data-testid="transaction-row"]')

    month_filter = (By.CSS_SELECTOR, '[data-testid="transaction-filter-month"]')
    year_filter = (By.CSS_SELECTOR, '[data-testid="transaction-filter-year"]')
    filter_submit = (By.CSS_SELECTOR, '[data-testid="transaction-filter-submit"]')

    detail_buttons = (By.CSS_SELECTOR, '[data-testid="transaction-detail-button"]')
    receipt_buttons = (By.CSS_SELECTOR, '[data-testid="transaction-receipt-button"]')

    report_download_button = (By.CSS_SELECTOR, '[data-testid="transaction-download-report"]')

    #action
    def open_index(self):
        self.driver.get(f"{BASE_URL}/transactions")
        self.wait.until(EC.visibility_of_element_located(self.table))

    def count_rows(self):
        return len(self.driver.find_elements(*self.rows))

    def filter_by_month_year(self, month, year):
        Select(self.wait.until(
            EC.element_to_be_clickable(self.month_filter)
        )).select_by_value(str(month))

        Select(self.wait.until(
            EC.element_to_be_clickable(self.year_filter)
        )).select_by_value(str(year))

        self.driver.find_element(*self.filter_submit).click()
        self.wait.until(EC.visibility_of_element_located(self.table))

    def click_new_transaction(self):
        self.wait.until(
            EC.element_to_be_clickable(self.new_transaction_button)
        ).click()

    def open_first_detail(self):
        self.wait.until(
            EC.presence_of_all_elements_located(self.detail_buttons)
        )[0].click()

    def open_first_receipt(self):
        self.wait.until(
            EC.presence_of_all_elements_located(self.receipt_buttons)
        )[0].click()

    def get_report_download_url(self):
        return self.driver.find_element(
            *self.report_download_button
        ).get_attribute("href")
    
    def download_report_pdf(self):
        self.wait.until(
            EC.element_to_be_clickable(self.report_download_button)
        ).click()