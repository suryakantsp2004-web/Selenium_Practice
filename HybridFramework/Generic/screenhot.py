
from datetime import datetime

def screenshot(driver):
    time_stamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    path = '../Defects'
    driver.save_screenshot(f"{path}/{time_stamp}.png")

