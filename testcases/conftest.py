import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from utilities.env_loader import load_env_config

@pytest.fixture
def config():
    return load_env_config()


@pytest.fixture
def driver(config):
    options = Options()
    # ✅ Disable Chrome password manager popups
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    # ✅ Disable the built-in breached password check popup
    options.add_argument("--disable-blink-features=PasswordManagerImplementation")

    # ✅ Optional: use incognito so no cookies, no saved passwords
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(config["implicit_wait"])
    driver.get(config["base_url"])
    yield driver
    driver.quit()
