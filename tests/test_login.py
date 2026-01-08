import pytest
from utils.driver import get_driver
from pages.login_page import LoginPage
from config.env import ADMIN_EMAIL, ADMIN_PASSWORD

LIMIT_TEST_EMAIL = "limit-test@example.com"

def test_login_valid(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)
    assert "dashboard" in driver.current_url


def test_login_invalid_email(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login("wrongemail@example.com", ADMIN_PASSWORD)
    assert "credentials" in login.get_error_message().lower()


def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, "wrongpassword")
    assert "credentials" in login.get_error_message().lower()


def test_login_attempts_limit(driver):
    login = LoginPage(driver)
    login.open_login()

    for _ in range(7):
        login.login(LIMIT_TEST_EMAIL, "wrongpassword")

    assert "too many" in login.get_error_message().lower()


def test_logout(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(ADMIN_EMAIL, ADMIN_PASSWORD)
    login.logout()

    assert "login" in driver.current_url
