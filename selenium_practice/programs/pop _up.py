from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
driver=Chrome(options=opts)
driver.maximize_window()

#js alerts
#simple alert
"""driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element("id","alertBtn").click()
sleep(3)
a=driver.switch_to.alert
a.accept()
sleep(3)"""

#Confirmation alert
"""driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("id","confirmBtn").click()
sleep(3)
a=driver.switch_to.alert
a.accept()
sleep(3)"""

"""driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element("id","confirmBtn").click()
sleep(3)
a=driver.switch_to.alert
a.dismiss()
sleep(3)"""
#prompt alert
"""driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.find_element("id","promptBtn").click()
alert=driver.switch_to.alert
msg = 'Suryakant'
alert.send_keys(msg)
alert.accept()
sleep(3)
user_text=driver.find_element("id","demo")
if msg in user_text.text:
    print("is present")
else:
    print("is absent")
driver.close()"""

#notification pop up
"""opts.add_argument("--disable-notifications")
opts.add_argument("--incognito")
opts.add_argument("--start-maximized")
driver.get("https://www.yatra.com/")"""

#hiddon popup
"""driver.get("https://www.shaadi.com/")
sleep(3)
driver.find_element("xpath","//button[text()='Login']").click()
sleep(3)
driver.find_element("name","email").send_keys("surya@123gmail.com")
driver.find_element("name","password").send_keys("12345")
sleep(3)
driver.find_element("xpath","//button[text()='Login with OTP']").click()
"""
"""driver.get("https://www.zomato.com/bangalore/")
driver.implicitly_wait(10)
driver.find_element("xpath","//a[text()='Log in']").click()
frame = driver.find_element("id","auth-login-ui")
driver.switch_to.frame(frame)
driver.find_element("xpath","//input[@inputmode='numeric']").send_keys("9373268523")
driver.find_element("xpath","//span[text()='Send One Time Password']").click()
boxes = driver.find_elements("xpath"," //input[@class='sc-hp56s6-1 jODXry']")
num = '987654'
for i in range(len(boxes)):
    boxes[i].send_keys(num[i])"""

#windows popups
#file upload
r"""driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
upload_btn=driver.find_element("id","singleFileInput")
file=r"C:\Users\Asus\Downloads\Resume QA.pdf"
upload_btn.send_keys(file)"""

r"""driver.get("https://www.naukri.com/registration/")
driver.implicitly_wait(10)
driver.find_element("xpath","//p[@class='main-2']").click()
up_btn=driver.find_element("id","resumeUpload")
file=r"C:\Users\Asus\Downloads\Resume QA.pdf"
up_btn.send_keys(file)"""

#file download
r"""path=r"C:\Users\Asus\OneDrive\Desktop\E1_ selenium\selenium_practice\.venv\selenium_downloads"
suryakant = {
    'safebrowsing.enabled':True,
    'download.default_directory':path
}
opts.add_experimental_option("prefs",suryakant)
driver=Chrome(options=opts)
driver.get("https://www.python.org/downloads/")
driver.implicitly_wait(10)
driver.find_element("xpath","//a[text()='Download Python install manager']").click()
"""
r"""from selenium.webdriver.support.select import Select
driver.get("https://demoapps.qspiders.com/ui/fileUpload?sublist=0")
driver.implicitly_wait(50)
driver.find_element("id","fullName").send_keys("suryakant")
driver.find_element("id","emailId").send_keys("suryakant@123gamil.com")
driver.find_element("id","password").send_keys("12345678")
driver.find_element("id","mobile").send_keys("9373268523")
city=driver.find_element("id","city")
ssd=Select(city)
ssd.select_by_index(1)
upload = driver.find_element("id","resume")
file=r"C:\Users\Asus\Downloads\Resume QA.pdf"
upload.send_keys(file)
driver.find_element("xpath","//option[text()='Javascript']").click()
driver.find_element("xpath","//label[text()='Receive job alerts according to your skills']").click()
driver.find_element("xpath"," //button[text()='Create Profile']").click()
"""
#chiled browser popup:
driver.get("https://demowebshop.tricentis.com/register")
driver.implicitly_wait(50)
links = driver.find_elements("xpath","//div[@class='column follow-us']//a")

for i in range(len(links)):
    if i == 2:
        continue
    else:
        links[i].click()
window = driver.window_handles
for i in window:
    driver.switch_to.window(i)
    print(driver.title)
    sleep(2)
    driver.close()
sleep(3)
print("all the links present")
driver.quit()
