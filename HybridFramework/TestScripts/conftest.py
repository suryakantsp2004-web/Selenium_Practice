from selenium.webdriver import Chrome,ChromeOptions
from Generic.verify_title import verify_title
import pytest
base_url = "https://demowebshop.tricentis.com/"

@pytest.fixture()
def setup():
    opts = ChromeOptions()
    opts.add_experimental_option("detach",True)
    driver = Chrome(opts)
    driver.get(base_url)
    driver.maximize_window()
    verify_title(driver,"Demo Web Shop")
    driver.implicitly_wait(10)
    yield driver
    driver.close()



