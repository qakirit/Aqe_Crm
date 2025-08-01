import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pythonProject1.pages.Customer_Group import CustomerGroupPage
from pythonProject1.pages.customer_group_edit import CustomerGroupEditPage
from selenium.webdriver.common.keys import Keys


class Promotional:
    promotional_button = (By.XPATH, "//a[@href='/promotional-code']")
    input_Promotional_Code = (By.XPATH, "//input[@name='code_name']")
    input_description = (By.XPATH, "//input[@name='description']")
    start_Date_button = (By.XPATH, "//div[contains(@class, 'MuiFormControl-root')]//input[@name='start_date']")
    input_start_Date = (By.XPATH, "//input[@name='start_date']")
    end_Date_button = (By.XPATH, "//label[text()='End Date  *']")
    input_end_date = (By.XPATH, "//input[@name='end_date']")
    select_Promotion_Types = (By.XPATH, "//label[text()='Select Promotion Types *']")
    input_select_promotion = (By.XPATH, "//li[@data-value='Single']")
    select_promotion_code = (By.XPATH, "//li[@data-value='All Customer']")
    Product_For_button = (By.XPATH, "//label[text()='Product For *']")
    select_Product_For_button = (By.XPATH, "//li[@data-value='All Products']")
    add_Promotional_Code = (By.XPATH, "//button[text()='Promotional Code']")
    eye_button = (By.XPATH, "(//button[contains(@class,'eye_btn')])[1]")
    edit_button = (By.XPATH, "(//button[contains(@class,'edit_btn')])[1]")
    delete_button = (By.XPATH, "//button[contains(@class,'delete_btn ')]")
    select_promotion_code_for_button = (By.XPATH, "//label[text()='Select Promotion Code For *']")
    select_project_button = (By.XPATH, "//label[text()='Select Product *']")
    input_discount_value = (By.XPATH, "//label[text()='Discount Value' ]")
    input_discount_type = (By.XPATH, "//label[text()='Discount Type*' ]")
    input_search = (By.XPATH, '//input[@placeholder="Search..."]')
    start_Date_container = (By.XPATH, "//div[contains(@class,'MuiInputBase-root') and .//input[@name='start_date']]")

    text = (By.XPATH,
            "//div[contains(@class, 'MuiInputBase-root') and contains(@class, 'Mui-focused')]//input[@type='date' and "
            "@name='start_date']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def Add_Promotion_code(self, data):
        self.wait_and_click(CustomerGroupPage.MARKETING)
        self.wait_and_click(self.promotional_button)
        self.wait_and_click(CustomerGroupPage.ADD_BUTTON)
        self.input_text(self.input_Promotional_Code, data["Promotion_code"])
        self.input_text(self.input_description, data["description"])

        date_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "start_date")))

        # Step 3: Scroll to the input (important in MUI forms)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", date_input)

        # Step 4: Use full JS injection to set value + fire events
        self.driver.execute_script("""
            const input = arguments[0];
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeInputValueSetter.call(input, "2025-07-31");
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
        """, date_input)

        self.wait_and_click(self.select_Promotion_Types)
        self.wait_and_click(self.input_select_promotion)

        self.wait_and_click(self.select_promotion_code_for_button)
        self.wait_and_click(self.select_promotion_code)

        self.wait_and_click(self.add_Promotional_Code)

        self.wait_and_click(CustomerGroupPage.ACTIVE_YES)

    def wait_and_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
