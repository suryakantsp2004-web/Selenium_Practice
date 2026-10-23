from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()
"""
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("id","name").send_keys("arbin")
sleep(3)
"""
"""driver.get("https://testautomationpractice.blogspot.com/")
sleep(4)
driver.find_element("id","name").send_keys("arbin")
driver.find_element("id","email").send_keys("arbin@gmail.com")
driver.find_element("id","phone").send_keys("1233567")
sleep(4)"""

"""driver.get("https://www.pizzahut.co.in/account/otp")
sleep(3)
driver.find_element("id","phone-field").send_keys("26754763247234")
"""
"""driver.get("https://www.pizzahut.co.in/account/otp")
sleep(3)
driver.find_element("class name","sc-fzokOt.kZxSHn").send_keys("26754763247234")
"""
"""driver.get("https://www.wikipedia.org/")
sleep(3)
driver.find_element("id","searchInput").send_keys("python selenium")
driver.find_element("class name","pure-button.pure-button-primary-progressive").click()
sleep(3)
"""
"""driver.get("https://demoqa.com/automation-practice-form")
sleep(3)
driver.find_element("tag name","input").send_keys("arbin")
sleep(5)
"""
"""driver.get("https://the-internet.herokuapp.com/")
sleep(3)
a=driver.find_element("tag name","h1")
print(a.text)
sleep(4)
"""
"""driver.get("https://the-internet.herokuapp.com/")
sleep(3)
a=driver.find_element("tag name","h1")
print(a.text)
sleep(4)
"""
"""driver.get("https://www.orangehrm.com/")
sleep(4)
driver.find_element("class name","email.text.tryit-email").send_keys("arbin@gmail.com")
sleep(3)
driver.find_element("class name","action.btn.btn-ohrm.btn-tryit-free").click()
sleep(4)
"""
"""driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("class name","inputtext._55r1._6luy").send_keys("arbin@gmail.com")
sleep(3)
driver.find_element("class name","inputtext._55r1._6luy._9npi").send_keys("1234")
sleep(3)
"""
"""driver.get("https://www.saucedemo.com/")
driver.find_element("class name","input_error.form_input").send_keys("arbin")
sleep(3)
driver.find_element("class name","input_error.form_input").send_keys("1234")
sleep(3)
driver.find_element("class name","input_error.form_input").send_keys("1234")
sleep(3)
"""
"""driver.get("https://www.saucedemo.com/")
sleep(3)
driver.find_element("name","user-name").send_keys("Suryakant")
driver.find_element("name","password").send_keys("123456")
sleep(3)
"""

"""driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
sleep(8)
driver.find_element("name","firstname").send_keys("Anu")
driver.find_element("name","lastname").send_keys("Saranya")
sleep(3)"""

"""driver.get("https://demoqa.com/automation-practice-form")
sleep(3)
driver.find_element("css selector","input[placeholder='Mobile Number']").send_keys("67889")
sleep(4)"""
"""driver.get("https://demowebshop.tricentis.com/register")
sleep(3)
driver.find_element("css selector","input[value='M']").click()
driver.find_element("css selector","input[name='FirstName']").send_keys("surya")
driver.find_element("css selector","input[id='LastName']").send_keys("s")
driver.find_element("css selector","input[name='Email']").send_keys("surya@123gmail.com")
driver.find_element("css selector","input[type='Password']").send_keys("123456")
driver.find_element("css selector","input[id='ConfirmPassword']").send_keys("123456")
driver.find_element("css selector","input[value='Register']").click()
sleep(5)
driver.close()
"""
"""driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("css selector","input[type='text'][name='email']").send_keys("surya@gmail.com")
driver.find_element("css selector","input[id='_R_66qjbjb9pb6amH1_'][type='password']").send_keys("123456")
driver.find_element("css selector","input[id=''][text='']").click()
sleep(4)
"""

driver.get("https://blinkit.com/")
sleep(3)
driver.find_element("xpath","//button[text()='Detect my location']").click()
sleep(3)
driver.find_element("xpath","//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']").click()
sleep(2)
driver.find_element("xpath","//input[@placeholder='Search for atta dal and more']").send_keys("milk")
sleep(3)
driver.find_element("xpath","//div[text()='Nandini Toned Milk']/ancestor::div[@class='tw-flex tw-w-full tw-flex-col']/descendant::div[text()='ADD']").click()








