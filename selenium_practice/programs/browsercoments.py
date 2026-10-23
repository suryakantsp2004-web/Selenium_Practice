#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
sleep(3)
driver.maximize_window()
sleep(3)
driver.close()
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
sleep(3)
driver.minimize_window()
sleep(3)
driver.close()
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
sleep(3)
driver.fullscreen_window()
sleep(3)
driver.close()
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://www.bookmyshow.com/")
driver.maximize_window()
sleep(3)
driver.minimize_window()
sleep(2)
driver.maximize_window()
sleep(3)
driver.close()
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(3)
driver.back()
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(3)
driver.back()
sleep(3)
driver.forward()
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
"""
driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(3)
driver.refresh()
"""
"""
driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
sleep(3)
size1=driver.get_window_size()
print("size 1:",size1)
driver.maximize_window()
size2=driver.get_window_size()
print("size2:",size2)
driver.close()
"""
"""
driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
sleep(3)
size1=driver.get_window_position()
print("size 1:",size1)
driver.maximize_window()
size2=driver.get_window_position()
print("size2:",size2)
driver.close() 
"""

"""
driver=Chrome(opts)
driver.get("https://www.tinder.com/")
sleep(3)
driver.back()
sleep(3)
driver.forward()
sleep(5)
driver.close()
"""








