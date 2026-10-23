from pom_package.loginpage import LoginPage

def test_TC1(setup):
    driver = setup
    login = LoginPage(driver)
    login.email_text_field("surya123@gmail.com")
    login.password_text_filed("surya@123")
    login.login_btn