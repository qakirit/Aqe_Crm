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