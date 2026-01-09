import pytest
from utils.driver import get_driver
from pages.login_page import LoginPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login_admin(driver):
    login = LoginPage(driver)
    login.open()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    return driver