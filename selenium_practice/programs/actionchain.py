from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()

"""a=ActionChains(driver)
driver.get("https://www.google.com/")
gmail=driver.find_element("xpath","//a[text()='Gmail']")
sleep(3)
a.click(gmail).perform()
sleep(3)"""
"""a=ActionChains(driver)
driver.get("https://www.google.com/")
gmail=driver.find_element("xpath","//a[text()='Gmail']")
sleep(3)
a.double_click(gmail).perform()
sleep(3)
"""
"""driver.get("https://demoqa.com/buttons")
sleep(3)
a=driver.find_element("id","rightClickBtn")
ac=ActionChains(driver)
sleep(3)
ac.context_click(a).perform()
sleep(3)
driver.close()"""

"""driver.get("https://share.google/NCZgBMRJlA4BwWQJJ")
sleep(3)
a=driver.find_element("xpath","//a[text()='Example code: Simple Context Menu']")
ac=ActionChains(driver)
sleep(3)
ac.context_click(a).perform()
sleep(3)
driver.close()"
"""
"""driver.get("https://www.amazon.com/")
sleep(3)
a=driver.find_element("xpath","//span[contains(text(),'Account & Lists')]")
ac=ActionChains(driver)
sleep(3)
ac.move_to_element(a).perform()
sleep(3)
driver.close()"""

"""driver.get("https://www.facebook.com/") 
sleep(3)
a=driver.find_element("id","_R_oiqjbjb9pb6amH1_")
ac=ActionChains(driver)
sleep(3)
ac.move_to_element(a).perform()
sleep(3)
driver.close()"""

"""driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
sleep(3)
driver.find_element("id","userName").send_keys("sss")
driver.find_element("id","password").send_keys("2345678")
a=driver.find_element("xpath","//img[@class='ng-star-inserted']")
ac=ActionChains(driver)
sleep(3)
ac.click_and_hold(a).perform()
sleep(3)
driver.close()"""

"""driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
sleep(3)
driver.find_element("id","userName").send_keys("sss")
driver.find_element("id","password").send_keys("2345678")
a=driver.find_element("xpath","//img[@class='ng-star-inserted']")
ac=ActionChains(driver)
sleep(3)
ac.click_and_hold(a).pause(8).release().perform()
sleep(3)"""

"""driver.get("https://demoqa.com/droppable")
sleep(3)
source=driver.find_element("id","draggable")
destination=driver.find_element("id","droppable")
ac=ActionChains(driver)
sleep(3)
ac.drag_and_drop(source,destination).perform()
sleep(3)"""

"""driver.get("https://testautomationpractice.blogspot.com")
sleep(3)
source=driver.find_element("id","draggable")
destination=driver.find_element("id","droppable")
ac=ActionChains(driver)
sleep(3)
ac.drag_and_drop(source,destination).perform()
sleep(3)"""

"""driver.get("https://www.amazon.com/")
sleep(3)
ac=ActionChains(driver)
driver.find_element("id","twotabsearchtextbox").click()
sleep(3)
ac.send_keys("iphone").perform()
sleep(3)
driver.close()"""

"""driver.get("https://www.flipkart.com/")
sleep(3)
ac=ActionChains(driver)
driver.find_element("name","q").click()
sleep(3)
ac.send_keys("iphone").perform()
sleep(3)
driver.close()"""

"""driver.get("https://www.amazon.com/")
sleep(3)
ac=ActionChains(driver)
a=driver.find_element("id","twotabsearchtextbox").click()
sleep(3)
ac.send_keys_to_element(a,"iphone").perform()
sleep(3)"""

"""driver.get("https://www.myntra.com/")
sleep(3)
ac=ActionChains(driver)
a=driver.find_element("xpath","//input[@placeholder='Search for products, brands and more']").click()
sleep(3)
ac.send_keys_to_element(a,"shoes").perform()
sleep(3)"""

"""driver.get("https://www.amazon.com/")
sleep(3)
ac=ActionChains(driver)
a=driver.find_element("xpath","//a[@class='nav_a']")
sleep(3)
ac.scroll_to_element(a).perform()
sleep(3)"""

from selenium.webdriver.common.keys import Keys
"""driver.get("https://www.facebook.com/")
ac=ActionChains(driver)
sleep(3)
driver.find_element("name","email").click()
sleep(3)
ac.key_down(Keys.SHIFT).send_keys("suryakant@123gmail.com").key_up(Keys.SHIFT).perform()
sleep(2)
driver.find_element("name","pass").click()
sleep(3)
ac.key_down(Keys.SHIFT).send_keys("suryakant").key_up(Keys.SHIFT).perform()
sleep(2)"""

"""driver.get("https://www.facebook.com/")
sleep(3)
ac=ActionChains(driver)
a=driver.find_element("xpath","//a[text()='Careers']")
sleep(3)
ac.key_down(
sleep(3)"""

"""driver.get("https://www.facebook.com/")
ac=ActionChains(driver)
sleep(3)
driver.find_element("name","email").click()
sleep(3)
ac.send_keys("Surya").perform()
ac.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
ac.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
driver.find_element("name","pass").click()
sleep(2)
ac.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
sleep(2)"""

"""driver.get("https://www.facebook.com/")
ac=ActionChains(driver)
sleep(3)
driver.find_element("name","email").click()
sleep(3)
ac.send_keys("Surya").perform()
sleep(3)
ac.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
ac.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
sleep(3)
ac.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
sleep(6)"""

"""driver.get("https://www.amazon.in/")
sleep(3)
ac=ActionChains(driver)
ac.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
sleep(4)
driver.close()"""








