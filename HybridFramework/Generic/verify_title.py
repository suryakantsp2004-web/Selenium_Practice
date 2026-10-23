from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Generic.screenhot import screenshot

def verify_title(driver,title):
    try:
        wait = WebDriverWait(driver,10)
        wait.until(EC.title_is(title))
        assert driver.title == title,screenshot(driver)
        print("Title Matched Successfully.....")
    except:
        screenshot(driver)
