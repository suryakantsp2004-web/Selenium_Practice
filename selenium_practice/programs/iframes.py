from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()

"""driver.get("https://vinothqaacademy.com/iframe/")
sleep(3)
driver.switch_to.frame(0)
sleep(3)
driver.find_element("id","nameInput").send_keys("sss")
sleep(3)"""
"""driver.switch_to.frame("employeetable")
sleep(3)
driver.find_element("id","nameInput").send_keys("sss")
sleep(3)"""
"""a=driver.find_element("xpath","//iframe[@title='Web Table']")
driver.switch_to.frame(a)

driver.find_element("id","nameInput").send_keys("sss")
sleep(3)"""


"""driver.switch_to.parent_frame()
sleep(3)
driver.switch_to.frame(2)
driver.find_element("xpath","//input[@id='vfb-5']").send_keys("sss")
sleep(2)
driver.close()"""

"""driver.switch_to.parent_frame()
sleep(3)
driver.switch_to.frame(1)
driver.find_element("xpath"," //button[text()='Alert Box']").click()
sleep(2)"""

driver.get("https://demowebshop.tricentis.com/register")
sleep(3)
driver.find_element("", "//a[contains(text(),'Books')][1]").click()






