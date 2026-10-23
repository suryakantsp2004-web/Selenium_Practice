from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.maximize_window()

"""driver.get("https://www.amazon.com/")
sleep(3)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(3)
a=driver.find_elements("xpath","//span[@class='s-heavy']")
for i in a:
    print(i.text)
"""
"""driver.get("https://lite.zeptonow.com/")
sleep(3)
driver.find_element("xpath","//span[text()='Search for']").click()
sleep(2)
driver.find_element("xpath","//input[@placeholder='Search for over 5000 products']").send_keys("milk")
sleep(3)
a=driver.find_elements("xpath","//li[@class='flex cursor-pointer items-center gap-x-2 py-2 font-semibold lg:px-4 transition-colors duration-300 hover:bg-gray-100 focus:bg-gray-100']")
for i in a:
    print(i.text)
sleep(3)
driver.quit()
"""
driver.get("https://www.flipkart.com/")
sleep(3)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(5)
driver.find_element("name","q").send_keys("iphone")
sleep(3)
a=driver.find_elements("xpath","//div[@class='VDtK0l _1psv1ze2u _1psv1ze53 _1psv1ze9x _1psv1ze7o']")
for i in a:
    print(i.text)

driver.quit()