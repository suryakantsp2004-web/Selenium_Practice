import pytest


"""from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)"""

#manually
"""@pytest.fixture
def thailand():
    print("Kempagowda IA")
    
def test_surya(thailand):
    print("Visit")

def test_aniket(thailand):
    print("To see places")
    
def test_ram(thailand):
    print("To enjoy")"""

#Automatic
"""@pytest.fixture(autouse=True)
def thailand():
    print("Kempagowda IA")
def test_surya(thailand):
    print("Visit")

def test_aniket(thailand):
    print("To see places")
    
def test_ram(thailand):
    print("To enjoy")"""

#two fixtures
"""@pytest.fixture
def thailand():
    print("Kempagowda IA")
    yield
    print("Return back to India")
@pytest.fixture
def airport():
    print("checking")
    yield
    print("you can go now")

 
def test_surya(thailand,airport):
    print("Visit")


def test_aniket(thailand,airport):
    print("To see places")


def test_ram(thailand,airport):
    print("To enjoy")
"""


"""@pytest.fixture(autouse=True)
def thailand():
    print("Kempagowda IA")
    yield
    print("Return back to India")


@pytest.fixture(autouse=True)
def airport():
    print("checking")
    yield
    print("you can go now")


def test_surya(thailand, airport):
    print("Visit")


def test_aniket(thailand, airport):
    print("To see places")


def test_ram(thailand, airport):
    print("To enjoy")
"""
#class level
#manual
"""@pytest.fixture(scope='class')
def check():
    print("Checking connection..")
    yield
    print("closing connection")
@pytest.mark.usefixtures("check")
class TestInstagram:
    def test_login(self):
        print("login is implemented successfully")
    def test_signup(self):
        print("signup is implemented successfully")
    def test_about(self):
        print("about is implemented successfully")"""

#automatic
"""@pytest.fixture(autouse=True)
def check():
    print("Checking connection..")
    yield
    print("closing connection")
@pytest.mark.usefixtures("check")
class TestInstagram:
    def test_login(self):
        print("login is implemented successfully")
    def test_signup(self):
        print("signup is implemented successfully")
    def test_about(self):
        print("about is implemented successfully")"""

#two class
"""@pytest.fixture(scope='class')
def check():
    print("Checking connection..")
    yield
    print("closing connection")
@pytest.mark.usefixtures("check")
class TestInstagram:
    def test_login(self):
        print("login is implemented successfully")
    def test_signup(self):
        print("signup is implemented successfully")
    def test_about(self):
        print("about is implemented successfully")
@pytest.mark.usefixtures("check")
class TestRapido():
    def test_bike(self):
        print("bike is implemented successfully")
    def test_car(self):
        print("car is implemented successfully")
    def test_bus(self):
        print("bus is implemented successfully")"""


"""@pytest.fixture(autouse=True)
def check():
    print("Checking connection..")
    yield
    print("closing connection")
@pytest.mark.usefixtures("check")
class TestInstagram:
    def test_login(self):
        print("login is implemented successfully")
    def test_signup(self):
        print("signup is implemented successfully")
    def test_about(self):
        print("about is implemented successfully")
@pytest.mark.usefixtures("check")
class TestRapido():
    def test_bike(self):
        print("bike is implemented successfully")
    def test_car(self):
        print("car is implemented successfully")
    def test_bus(self):
        print("bus is implemented successfully")"""

from selenium.webdriver import Chrome,ChromeOptions

@pytest.fixture
def setup():
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_login(setup):
    driver = setup
    driver.find_element("xpath","//a[text()='Log in']").click()
    driver.find_element("xpath","//input[@value='Log in']").click()

def test_register(setup):
    driver = setup
    driver.find_element("xpath","//a[text()='Register']").click()
    driver.find_element("id", "register-button").click()




