from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
"""
print("Available browser comments---\n1.Display browser size\n2.display browser position\n3.set browser size\n4.set browser position")
choice = int(input("Enter choice: "))
if choice == 1:

    driver = Chrome(opts)
    sleep(3)
    size1 = driver.get_window_size()
    print("size",size1)
    driver.close()
elif choice == 2:

    driver = Chrome(opts)
    sleep(3)
    position1 = driver.get_window_positon()
    print("position1", position1)
    driver.close()
elif choice == 3:
    x = int(input("Enter the width:"))
    y = int(input("Enter the height:"))

    driver = Chrome(opts)
    sleep(3)
    size = driver.set_window_size(x,y)
    print("size",size)
elif choice == 4:
    x = int(input("Enter the width:"))
    y = int(input("Enter the height:"))

    driver = Chrome(opts)
    sleep(3)
    position = driver.set_window_position(x, y)
    print("position", position)
   """
"""
driver = Chrome(opts)
driver.get("https://www.zepto.com/")
sleep(3)
width = int(input("Enter Browser width:"))
height = int(input("Enter Browser height:"))
driver.get_window_size(width , height)
"""
"""
driver = Chrome(opts)
driver.get("https://www.zepto.com/")
driver.maximize_window()
sleep(3)
x = int(input("Enter Browser x position:"))
y = int(input("Enter Browser y position:"))
driver.get_window_position(x,y)
"""
driver = Chrome(opts)
driver.get("https://www.zomato.com/")
driver.maximize_window()
sleep(5)
driver.refresh()
size = driver.get_window_size()
print("size:",size)
driver.set_window_size(800,600)
driver.set_window_position(200,100)
driver.refresh()
driver.back()
sleep(3)
driver.close()






