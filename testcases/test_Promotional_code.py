import os
import time

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

    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    add_promotion_value = f"{Add_Promotion_code['Add_Promotion']}_{timestamp}"  # first line comming from ymal table+ join time formte
    Add_Promotion_code["Add_Promotion"] = add_promotion_value  # now Add_Promotion value has been changed.

    page.Add_Promotion_code_page(Add_Promotion_code)
    actual_message = page.wait.until(EC.visibility_of_element_located(page.add_promo_code_toast))

    assert "Promotional Code created successfully." in actual_message.text


@pytest.mark.parametrize("Add_Promotion_code", load_groups())
def test_Inactive_Promotion(driver, config, Add_Promotion_code):
    login_page = SignIn(driver)
    login_page.sign_in(config["username"], config["password"])

    page = Promotional(driver)

    page.Inactive_Promotion()
    actual_message = page.wait.until(EC.visibility_of_element_located(page.add_promo_code_toast))

    assert "Promotional code status updated successfully." in actual_message.text

