from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sign_in:
    email = "email"
    password = "password"
    sign_in_button = "//button[text()='sign in']"
    exp_dashboard_text = "//span[text()='dashboard']"
    logout_button ="//button[@aria-label='Logout']"
    logout_yes = "//button[text()='Yes, Logout!']"
    sign_in_text = "//h4[text()='Sign in']"
    welcome_text="//div[@class='Toastify__toast-container Toastify__toast-container--top-right']"
    welcome_close= "//button[@class='Toastify__close-button Toastify__close-button--colored']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def sign_in(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.email))).send_keys(email)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.password))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.welcome_text)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.welcome_close))).click()



