from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
driver=Chrome(options=opts)
driver.maximize_window()

#was to take screenshot
"""driver.get("https://demowebshop.tricentis.com/register")
sleep(3)
driver.save_screenshot("defect.png")
driver.close()"""

#was to screenshot store in specific folder:
"""path = "../Defect"
driver.get("https://www.flipkart.com/")
sleep(3)
driver.save_screenshot(f"{path}/defect.png")
driver.close()"""

#extract the current datetime
"""from datetime import datetime
current_dt = datetime.now()
print(current_dt)
"""
#format the datetime:
"""from datetime import datetime
time_stamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
print(time_stamp)"""

#implimenting time stamp in the screenshot:
"""from datetime import datetime
path = "../Defect"
time_stamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
driver.get("https://www.amazon.in/")
sleep(3)
driver.save_screenshot(f"{path}/{time_stamp}.png")
driver.close()"""

from datetime import datetime
def screenshot(driver):
    path = "../Defect"
    time_stamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    driver.save_screenshot(f"{path}/{time_stamp}.png")
def verify_url(driver,url):
    assert url in driver.current_url,screenshot(driver)
    print("Url verified successfully")
base_url = "https://practicetestautomation.com/practice-test-login/"
driver.get(base_url)
driver.implicitly_wait(50)
verify_url(driver,base_url)
driver.find_element("id","username").send_keys("student")
driver.find_element("id","password").send_keys("Password123")
driver.find_element("xpath","//button[text()='Submit']").click()
verify_url(driver,"practicetestautomation.com/logged-in-successfully/")
assert 'Congratulations' in driver.page_source,screenshot(driver)
print("Text is present")
logout_btn = driver.find_element("xpath","//a[text()='Log out']")
assert logout_btn.is_displayed,screenshot(driver)
print("button displayed successfully")
logout_btn.click()
verify_url(driver,base_url)
print("Test case1 passed successfully")
driver.close()