import time

import pytest
from pages.sign_in_page import Sign_in
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.sign
class TestSign:

    @pytest.mark.title
    def test_title(self, driver):
        login_page = Sign_in(driver)
        assert driver.title == "QeTeam CRM"

    @pytest.mark.login
    def test_valid_login(self, driver, config):
        login_page = Sign_in(driver)
        login_page.sign_in(config["username"], config["password"])
        dashboard = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, login_page.exp_dashboard_text))
        )
        login_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, login_page.welcome_text)))
        assert "Welcome back! You're now logged in." in login_text.text

    @pytest.mark.logout
    def test_logout(self, driver, config):
        login_page = Sign_in(driver)
        login_page.sign_in(config["username"], config["password"])
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, login_page.logout_button))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, login_page.logout_yes))).click()
        sign_text = wait.until(EC.visibility_of_element_located((By.XPATH, login_page.sign_in_text)))
        assert "Sign in" in sign_text.text
