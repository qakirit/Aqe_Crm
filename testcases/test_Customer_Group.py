import os
import pytest
import yaml
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from pages.Customer_Group import CustomerGroupPage
from pages.sign_in_page import Sign_in



def load_groups():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "../configuration/customer_groups.yaml")
    with open(file_path) as f:
        return yaml.safe_load(f)["groups"]


@pytest.mark.parametrize("group_data", load_groups())
def test_create_customer_group(driver, config, group_data):
    login_page = Sign_in(driver)
    login_page.sign_in(config["username"], config["password"])

    page = CustomerGroupPage(driver)

    # Generate unique group name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_group_name = f"{group_data['name']}_{timestamp}"
    group_data["name"] = unique_group_name

    page.create_customer_group(group_data)

    # Wait for success toast and assert
    toast = page.wait.until(EC.visibility_of_element_located(page.customer_successfully_text))
    assert "Customer group created successfully." in toast.text
