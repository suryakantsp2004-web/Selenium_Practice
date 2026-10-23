import pytest

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)

@pytest.mark.parametrize("un,pwd",[['suryakant@134gmail.com','78123'],['aniket212@gmail.com','78961234']])
def test_demo(un,pwd):
    driver = Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/login")
    driver.maximize_window()
    driver.implicitly_wait(100)
    driver.find_element("id","Email").send_keys(un)
    driver.find_element("id","Password").send_keys(pwd)
    driver.find_element("xpath", "//input[@value='Log in']").click()
    driver.close()