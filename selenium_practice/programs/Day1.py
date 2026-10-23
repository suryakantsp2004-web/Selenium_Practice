"""
from selenium.webdriver import Chrome
from time import sleep
Chrome()
sleep(5)
"""

#
"""
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
c = Chrome(opts)
print("Browser Launched Successfully!!!")
"""


#
"""
from selenium.webdriver import Chrome, ChromeOptions,Edge,EdgeOptions,Firefox
Print("Available Browser---\n1.chrome\n2.Firefox\n3.Edge")
choice = int(input("Enter your choice:"))
if choice == 1:
    chrome()
    Print("chrome Launched Successfully")
elif choice == 3:
    Edge()
    print("Edge Launched Successfully")
elif choice == 2:
    Firefox()
    print("Firefox Launched Successfully")
else:
    print("Wrong Choice")
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = chromeOptions()
opts.add_experimental_option("detach", True)
c = chrome(opts)
sleep(3)
c.close()
"""
#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = chromeOptions()
opts.add_experimental_option("detach", True)
c = chrome(opts)
sleep(3)
c.quite()
"""

#
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
c=Chrome(options=opts)
c.get("https://www.amazon.in/")
sleep(3)
c.get("https://www.flipkart.com/")
"""
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

choice = int(input("Enter your choice:"))
if choice == 1:
    c = Chrome(options=opts)
    c.get("https://www.amazon.in/")
elif choice == 2:
    c = Chrome(options=opts)
    c.get("https://www.flipkart.com/")
elif choice == 3:
    c = Chrome(options=opts)
    c.get("https://www.myntra.com/")
else:
    print("Wrong Choice")
    """
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
"""
driver = Chrome(opts)
driver.get("https://www.bookmyshow.com/explore/home/bengaluru")
sleep(3)
size_position1=driver.get_window_rect()
print("size_position1:",size_position1)
driver.maximize_window()
size_position2=driver.get_window_rect()
print("size_position2:",size_position2)
sleep(3)
driver.close()
"""
"""
driver = Chrome(opts)
driver.get("https://www.bookmyshow.com/explore/home/bengaluru")
sleep(3)
driver.set_window_size(900,800)
print("Browser size changed")
"""
"""
driver = Chrome(opts)
driver.get("https://www.bookmyshow.com/explore/home/bengaluru")
sleep(3)
driver.set_window_position(40,40)
print("Browser position changed")
"""
"""
driver = Chrome(opts)
driver.get("https://www.bookmyshow.com/explore/home/bengaluru")
sleep(3)
driver.set_window_rect(600,400,100,100)
print("Browser position and size changed")
"""
"""
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
title = driver.title
print("Title:",title)
driver.close()
"""
"""
expected_title="Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
title = driver.title
if title == expected_title:
    print("Testcase Passed")
else:
    print("Testcase Failed")
driver.close()
"""
"""
url = "https://www.amazon.in/"
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
new_url = driver.current_url
print(new_url)
if url == new_url:
    print("Testcase passed")
else:
    print("Testcase Failed")
driver.close()
"""
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
source = driver.page_source
print(source)
driver.close()



