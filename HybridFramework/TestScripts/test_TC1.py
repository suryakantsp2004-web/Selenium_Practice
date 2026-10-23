from POM.loginpage import LoginPage
from POM.homepage import HomePage
from Generic.verify_title import verify_title
from Utilities.XLUtils import read_data
import pytest
path = "../ExcelFiles/demo.xlsx"
data = read_data(path,"inputs")

@pytest.mark.parametrize("un,pwd,exp_url",data)
def test_TC1(setup,un,pwd,exp_url):
    driver = setup
    hp = HomePage(driver)
    login = LoginPage(driver)
    hp.login_link()
    login.username_text_field(un)
    login.password_text_field(pwd)
    login.login_btn()
    verify_title(driver,exp_url)







