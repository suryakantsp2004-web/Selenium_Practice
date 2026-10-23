from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
sleep(3)
driver.find_element("css selector","input[value='M']").click()
driver.find_element("css selector","input[name='FirstName']").send_keys("surya")
driver.find_element("css selector","input[id='LastName']").send_keys("s")
driver.find_element("css selector","input[name='Email']").send_keys("suryakant@123gmail.com")
driver.find_element("css selector","input[type='Password']").send_keys("123456")
driver.find_element("css selector","input[id='ConfirmPassword']").send_keys("123456")
driver.find_element("css selector","input[value='Register']").click()
sleep(5)
driver.find_element("xpath","//a[text()='Log in']").click()
sleep(3)
driver.find_element("id","Email").send_keys("suryakant@123gmail.com")
driver.find_element("id","Password").send_keys("123456")
driver.find_element("id","RememberMe").click()
driver.find_element("css selector","input[class='button-1 login-button']").click()
sleep(3)
driver.find_element("xpath","//a[href='/computers'][1]").click()
sleep(3)
driver.find_element("xpath","a[@href='/desktops'][1]").click()
sleep(3)






