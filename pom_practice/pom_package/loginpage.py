class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def email_text_field(self, un):
        self.driver.find_element("id", "Email").send_keys(un)

    def password_text_filed(self, pwd):
        self.driver.find_element("id", "Password").send_keys(pwd)

    def login_btn(self):
        self.driver.find_element("xpath", "//input[@value='Log in']").click()
