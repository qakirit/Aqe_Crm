import os
import pytest
import yaml
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from pythonProject1.pages import Customer_Group
from pythonProject1.pages import sign_in_page
from pythonProject1.pages.Customer_Group import CustomerGroupPage
from pythonProject1.pages.sign_in_page import SignIn
from pythonProject1.pages.Promotional_Code_page import Promotional


def load_groups():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "../configuration/Promotion_code.yaml")
    with open(file_path) as f:
        return yaml.safe_load(f)["Add_Promotion_code"]


@pytest.mark.parametrize("Add_Promotion_code", load_groups())
def test_Add_Promotion_code(driver, config, Add_Promotion_code):
    login_page = SignIn(driver)
    login_page.sign_in(config["username"], config["password"])

    page = Promotional(driver)

    page.Add_Promotion_code(Add_Promotion_code)

    # Wait for success toast and assert
    #toast = page.wait.until(EC.visibility_of_element_located(page.customer_successfully_text))
    #assert "Customer group created successfully." in toast.text
