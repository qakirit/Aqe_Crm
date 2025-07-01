from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerGroupPage:
    # ===============================
    # Locators
    # ===============================
    MARKETING = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-zws9p5']/div[5]")
    CUSTOMERGROUP_LINK = (By.XPATH, "//a[@title='Customer Group']")
    ADD_BUTTON = (By.XPATH, "//button[@aria-label='Add']")
    SELECT_CUSTOMER_TYPE = (By.XPATH, "//label[text()='Select Customer Type']")
    SELECT_TYPE_MEMBER = (By.XPATH, "//span[text()='Member']")
    RADIOBUTTON_CREATE_NEW_GROUP = (By.XPATH, "//span[text()='Create new group']")
    CUSTOMER_GROUP_NAME = (By.XPATH, "//input[@name='name']")
    ACTIVE_YES = (By.XPATH, "//span[text()='Yes']")
    FINISH_BUTTON = (By.XPATH, "//button[text()='Finish']")

    # Date and amount fields
    CUSTOMER_SIGNED_FROM_DATE = (By.XPATH, "//input[@name='customer_signup_from_date']")
    CUSTOMER_SIGNED_UP_DATE = (By.XPATH, "//input[@name='customer_signup_to_date']")
    AMOUNT_PAID_TILL_DATE = (By.XPATH, "//input[@name='amount_paid_till_from']")
    AMOUNT_PAID_TILL_TO = (By.XPATH, "//input[@name='amount_paid_till_to']")
    AMOUNT_OUTSTANDING_TILL_FROM = (By.XPATH, "//input[@name='amount_outstanding_till_from']")
    AMOUNT_OUTSTANDING_TILL_TO = (By.XPATH, "//input[@name='amount_outstanding_till_to']")
    NUMBER_OF_MIN_ORDERS = (By.XPATH, "//input[@name='number_of_min_orders']")
    NUMBER_OF_MAX_ORDERS = (By.XPATH, "//input[@name='number_of_max_orders']")
    MIN_BUSINESS_AMOUNT = (By.XPATH, "//input[@name='min_business_amount']")
    MAX_BUSINESS_AMOUNT = (By.XPATH, "//input[@name='max_business_amount']")
    LAST_ORDER_DATE = (By.XPATH, "//input[@name='last_order_date']")
    NUMBER_OF_ORDERS_AT_LAST = (By.XPATH, "//input[@name='number_of_orders_at_last']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    customer_successfully_text = (
        By.XPATH, "//div[@class='Toastify__toast-body']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def navigate_to_customer_group(self):
        self.wait_and_click(self.MARKETING)
        self.wait_and_click(self.CUSTOMERGROUP_LINK)
        self.wait_and_click(self.ADD_BUTTON)

    def select_customer_type(self):
        # Click dropdown
        element = self.wait.until(EC.element_to_be_clickable(self.SELECT_CUSTOMER_TYPE))
        self.actions.move_to_element(element).click().perform()

        # Wait specifically for dropdown options to be visible
        self.wait.until(EC.visibility_of_element_located(self.SELECT_TYPE_MEMBER))

        # Now click the member type
        self.wait_and_click(self.SELECT_TYPE_MEMBER)

    def fill_customer_group_details(self, data):
        self.input_text(self.CUSTOMER_SIGNED_FROM_DATE, data["signup_from_date"])
        self.input_text(self.CUSTOMER_SIGNED_UP_DATE, data["signup_to_date"])
        self.input_text(self.AMOUNT_PAID_TILL_DATE, data["paid_from"])
        self.input_text(self.AMOUNT_PAID_TILL_TO, data["paid_to"])
        self.input_text(self.AMOUNT_OUTSTANDING_TILL_FROM, data["outstanding_from"])
        self.input_text(self.AMOUNT_OUTSTANDING_TILL_TO, data["outstanding_to"])
        self.input_text(self.NUMBER_OF_MIN_ORDERS, data["min_orders"])
        self.input_text(self.NUMBER_OF_MAX_ORDERS, data["max_orders"])
        self.input_text(self.MIN_BUSINESS_AMOUNT, data["min_business"])
        self.input_text(self.MAX_BUSINESS_AMOUNT, data["max_business"])
        self.input_text(self.LAST_ORDER_DATE, data["last_order_date"])
        self.input_text(self.NUMBER_OF_ORDERS_AT_LAST, data["last_order_count"])

    def finalize_group_creation(self, group_name):
        self.wait_and_click(self.NEXT_BUTTON)
        self.wait_and_click(self.RADIOBUTTON_CREATE_NEW_GROUP)
        self.input_text(self.CUSTOMER_GROUP_NAME, group_name)
        self.wait_and_click(self.ACTIVE_YES)
        self.wait_and_click(self.FINISH_BUTTON)

    def create_customer_group(self, data):
        self.navigate_to_customer_group()
        self.select_customer_type()
        self.fill_customer_group_details(data)
        self.finalize_group_creation(data["name"])

    def wait_and_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
