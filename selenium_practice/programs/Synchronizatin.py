from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()

#Static wait
"""driver.get("https://www.shoppersstack.com/")
sleep(7)
driver.find_element("xpath","//button[text()='Login']").click()
sleep(6)
driver.find_element("id","Email").send_keys("ss@gamil.com")
driver.find_element("id","Password").send_keys("123445")
sleep(4)
driver.find_element("xpath","//span[text()='Login']").click()
driver.close()"""

#imlicitly wait
"""driver.implicitly_wait(1000)
driver.get("https://www.shoppersstack.com/")
driver.find_element("xpath","//button[text()='Login']").click()
driver.find_element("id","Email").send_keys("ss@gamil.com")
driver.find_element("id","Password").send_keys("123445")
driver.find_element("xpath","//span[text()='Login']").click()
"""
#explycite wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""driver.implicitly_wait(1000)
driver.get("https://www.shoppersstack.com/products_page/87")
driver.find_element("id","Check Delivery").send_keys("560037")
a=driver.find_element("id","Check")
ob=WebDriverWait(driver,100)
ob.until(EC.element_to_be_clickable(a))
a.click()"""












