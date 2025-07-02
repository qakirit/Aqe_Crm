import os
import pytest
from pages.sign_in_page import SignIn
from pages.customer_group_edit import CustomerGroupEditPage
from pages.Customer_Group import CustomerGroupPage


@pytest.mark.customer_group_edit
def test_edit_customer_group(driver, config):
    # 1. Login
    login_page = SignIn(driver)
    login_page.sign_in(config["username"], config["password"])

    # 2. Navigate to Customer Group page
    customer_group_page = CustomerGroupPage(driver)
    customer_group_page.navigate_to_customer_group()

    # 3. Initialize CustomerGroupEditPage
    edit_page = CustomerGroupEditPage(driver)
    edit_page.click_edit_button()

    # 4. Edit flow - Click edit and toggle status
    edit_page.click_remove_button()  # perform click only

    toast_msg = edit_page.confirm_alert()  # fetch toast text
    assert "Please select a customer from the list" in toast_msg





