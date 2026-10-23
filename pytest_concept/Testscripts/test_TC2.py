"""import pytest
pytestmark = pytest.mark.sanity

def test_case1():
    print("test_case1 is executing")

class Testdemo:
    def test_case2(self):
        print("test_case 2 is executing")
    def test_case3(self):
        print("test_case 3 is executing")"""
#conftest
def test_register(setup):
    driver = setup
    driver.find_element("xpath","//a[text()='Register']").click()
    driver.find_element("id", "register-button").click()