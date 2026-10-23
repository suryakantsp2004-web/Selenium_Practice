 

#Markaer module level
"""import pytest
pytestmark = pytest.mark.smoke

def test_case1():
    print("test_case1 is executing")"""



#conftest
def test_login(setup):
    driver = setup
    driver.find_element("xpath","//a[text()='Log in']").click()
    driver.find_element("xpath","//input[@value='Log in']").click()