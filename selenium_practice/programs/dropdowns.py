from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.select import Select
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

"""driver = Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(3)
country = driver.find_element("id","country")
ssd= Select(country)
ssd.select_by_index(3)
"""
"""driver =Chrome(opts)
driver.get("https://demoqa.com/select-menu")
sleep(3)
driver.maximize_window()
a=driver.find_element("id","cars")
ob=Select(a)
ob.select_by_visible_text("Audi")
sleep(3)
ob.select_by_index(0)
ob.select_by_value("opel")
ob.select_by_visible_text("Saab")
sleep(3)
"""

"""ob.deselect_by_index(3)
sleep(3)
ob.deselect_by_value("volvo")
sleep(3)
ob.deselect_by_visible_text("Opel")
sleep(3)
ob.deselect_by_visible_text("Saab")
"""
"""ob.deselect_all()
sleep(3)
driver.quit()
"""
#multi select dropdown
driver = Chrome(opts)
driver.get("https://www.qaplayground.com/practice/dropdowns")
sleep(2)
driver.maximize_window()
# Locate multi-select dropdown
msg = driver.find_element("id", "dropdown-fruit").click()
msg_obj = Select(msg)
sleep(2)
# Check if it supports multiple selection
msg_obj.select_by_index(0)
msg_obj.select_by_index(1)
msg_obj.select_by_index(2)

# Print selected values
selected = msg_obj.all_selected_options
for i in selected:
    print(i.text)
sleep(3)

driver.close()

#non standered dropdown
"""driver =Chrome(opts)
driver.get("https://demoqa.com/select-menu")
sleep(3)
driver.maximize_window()
driver.find_element("xpath","//div[@class='css-19bb58m']").click()
sleep(3)
driver.find_element("xpath","//div[text()='Group 1, option 2']").click()
sleep(4)
driver.quit()
"""
"""driver =Chrome(opts)
driver.get("https://www.qaplayground.com/practice/dropdowns")
sleep(3)
driver.maximize_window()
driver.find_element("id","dropdown-fruit").click()
sleep(3)
driver.find_element("xpath","//span[text()='Banana']").click()
sleep(3)
driver.find_element("id","dropdown-country").click()
sleep(4)
driver.find_element("xpath"," //span[text()='USA']").click()
sleep(3)
driver.quit()"""


