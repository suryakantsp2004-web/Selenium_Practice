
from Utilities.XLUtils import *

path = '../ExcelFiles/demo.xlsx'
loc = read_locators(path,"locators")


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def username_text_field(self,un):
        self.driver.find_element(*loc['username_tf']).send_keys(un)
    def password_text_field(self,pwd):
        self.driver.find_element(*loc['password_tf']).send_keys(pwd)

    def login_btn(self):
        self.driver.find_element(*loc['submit_btn']).click()