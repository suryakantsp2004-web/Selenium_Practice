from Utilities.XLUtils import read_locators

path = "../ExcelFiles/demo.xlsx"

loc = read_locators(path,"locators")

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def login_link(self):
        self.driver.find_element(*loc['login_link']).click()