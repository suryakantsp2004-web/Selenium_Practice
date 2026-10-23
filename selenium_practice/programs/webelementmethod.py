from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()

"""driver.get("https://www.flipkart.com/")
sleep(3)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(2)
search_tf=driver.find_element("name","q")
search_tf.send_keys("realme p1")
sleep(3)
search_tf.clear()
search_tf.send_keys("iphone")
sleep(4)
driver.close()
"""
"""driver.get("https://www.flipkart.com/")
sleep(3)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(2)
search=driver.find_element("name","q")
search.send_keys("iphone")
sleep(3)
search.submit()
driver.close()
"""
"""driver.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand&gclsrc=aw.ds&gad_source=1&gad_campaignid=19863995494&gbraid=0AAAAADLp3cE2xMhOs9pUeyaAIGoEtsPvN&gclid=Cj0KCQjws83OBhD4ARIsACblj1_pPDVHCu38STl85DrtRKf7MIb_AX4BTa43GOtEFzH1WByAxPFZ07IaAuD1EALw_wcB")
sleep(3)
driver.find_element("css selector","input[id=name]").send_keys("surya")
driver.find_element("css selector","input[id=email]").send_keys("surya@123gmail.com")
driver.find_element("css selector","input[id=password]").send_keys("surya@123")
driver.find_element("css selector","input[id=mobile]").send_keys("1234567892")
driver.find_element("xpath","//div[@role='radio']").click()

reg_btn=driver.find_element("xpath","//button[text()='Register now']")
if reg_btn.is_enabled():
    reg_btn.click()
else:
    print("Button is not enabled")
driver.close()"""
"""driver.get("https://demowebshop.tricentis.com/")
sleep(3)
excellent_radio = driver.find_element("xpath","//input[@id='pollanswers-1']")
print("Before:",excellent_radio.is_selected())
sleep(2)
excellent_radio.click()
print("After:",excellent_radio.is_displayed())"""

"""driver.get("https://demowebshop.tricentis.com/")
sleep(3)
driver.find_element("link text",'Log in').click()
sleep(3)
try:
    error_msg = driver.find_element("xpath","//div[@class='validation-summary-errors']")
    print(error_msg.is_displayed())
except:
    print("Message Not displayed")
driver.find_element("xpath"," //input[@value='Log in']").click()
sleep(3)
error_msg = driver.find_element("xpath","//div[@class='validation-summary-errors']")
print(error_msg.is_displayed())
"""

"""driver.get("https://www.wikipedia.org/")
sleep(3)
english = driver.find_element("xpath","//a[@id='js-link-box-en']")
print("Tool Tip:",english.get_attribute("title"))
print("Link:",english.get_attribute("href"))
driver.close()
"""
def verify_title(driver,title):
    if driver.title == title:
        print("Title verified successfully")
    else:
        print("No verified")
driver.get("https://demowebshop.tricentis.com/")
verify_title(driver,"Demo Web Shop")
sleep(3)
register = driver.find_element("xpath","//a[text()='Register']")
if register.is_displayed():
    register.click()
    verify_title(driver,"Demo web shop. Register")
    male = driver.find_element("id","gender-male")
    if male.is_displayed():
        male.click()
    if male.is_selected():
        fn = driver.find_element("id","FirstName")
        if fn.is_displayed():
            fn.send_keys("suryakant")
            ln = driver.find_element("id","LastName")
            if ln.is_displayed():
                ln.send_keys("S")
                email = driver.find_element("id","Email")
                if email.is_displayed():
                    email.send_keys("surya@123gmail.com")
                    pwd = driver.find_element("id","Password")
                    if pwd.is_displayed():
                        pwd.send_keys("123456")
                        cpwd = driver.find_element("id","ConfirmPassword")
                        if cpwd.is_displayed():
                            cpwd.send_keys("123456")
                            reg = driver.find_element("id","register-button")
                            if reg.is_displayed():
                                reg.click()


    else:
        print("not displayed")
else:
    print("Register Not displayed")
driver.close()






