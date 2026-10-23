from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()
"""driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
driver.find_element("css selector","input[id='name']").send_keys("surya")
driver.find_element("css selector","input[id='email']").send_keys("surya@123gmail.com")
driver.find_element("css selector","input[id='password']").send_keys("123456789")
driver.find_element("css selector","button[type='submit']").click()
sleep(2)
driver.close()
"""
"""driver.get("https://www.example.com/")
sleep(3)
links = driver.find_elements("tag name", "a")
for link in links:
    href = link.get_attribute("href")
    if href:
        print(href)
driver.close()
"""

"""driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
A=driver.find_elements("xpath","//input")
print(len(A))
sleep(2)
driver.quit()
"""
# 4
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# A=driver.find_elements('tag name','img')
# print(len(A))
# driver.quit()

# 5
# //tagname[text()='exact text']
# //tagname[@attribute='value']
# //tagname[contains(@attribute,'value')]
# (xpath)[index]
# //tagname[contains(text(),'partial text')]


# 6
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# driver.find_element('css selector','#name').send_keys("Asish kumar pradhan")
# driver.find_element('css selector','#email').send_keys("asish23@GMAIL.COM")
# driver.find_element('css selector','#phone').send_keys("Asish kumar pradhan")
# driver.find_element('css selector','#textarea').send_keys("Asish kumar pradhan")
# driver.find_element('xpath','//label[@for="male"]').click()
# driver.find_element('xpath','//label[@for="monday"]').click()
# driver.find_element('xpath','//label[@for="tuesday"]').click()
# driver.find_element('xpath','//label[@for="wednesday"]').click()
# sleep(2)
# driver.quit()

# 7
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# driver.find_element('xpath',"//input[@name='email']").send_keys("asish@2gmail.com")
# driver.find_element('xpath',"//input[@name='pass']").send_keys("asish@2gmail.com")
# driver.find_element('xpath',"//div[@role='none']").click()
# sleep(2)
# driver.quit()
"""driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("id","name").send_keys("suryakant")
driver.find_element("id","email").send_keys("surya@123gmail.com")
driver.find_element("id","phone").send_keys("9373268523")
driver.find_element("id","textarea").send_keys("Marathahalli")
driver.find_element("id","male").click()
driver.find_element("id","monday").click()
driver.find_element("id","tuesday").click()
driver.find_element("id","wednesday").click()
driver.find_element("id","thursday").click()
driver.find_element("id","friday").click()
driver.find_element("id","saturday").click()
driver.find_element("id","country").click()
driver.find_element("tag name","india",).click()
sleep(3)
driver.close()
"""
"""driver.get("https://www.redbus.in/")
sleep(2)
srcinput=wait.until driver.find_element("id", "srcinput").send_keys("Bengaluru")
sleep(3)
driver.find_element("id", "destinput").send_keys("Tumakuru")
sleep(2)
driver.find_element("xpath","//button[text()='Search buses']").click()"""

driver.get("https://vinothqaacademy.com/iframe/")
sleep(2)
driver.find_element("id","nameInput").send_keys("sss")
sleep(3)
driver.find_element("name","alertbox").click()
sleep(3)
driver.find_element("id","vfb-5").send_keys("sss")
driver.close()
