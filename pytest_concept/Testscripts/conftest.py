


import pytest
from selenium.webdriver import Chrome,ChromeOptions
@pytest.fixture
def setup():
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()