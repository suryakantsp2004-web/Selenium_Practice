# function level

import pytest
"""@pytest.mark.smoke
def test_login():
    print("login is implemented successfully")
@pytest.mark.smoke
def test_signup():
    print("signup is implemented successfully")
@pytest.mark.smoke
def test_contact():
    print("contact is implemented successfully")
    
    collected 3 items                                                                                                                                  

markers.py::test_login login is implemented successfully
PASSED
markers.py::test_signup signup is implemented successfully
PASSED
markers.py::test_contact contact is implemented successfully
PASSED
"""

"""@pytest.mark.smoke
def test_login():
    print("login is implemented successfully")
@pytest.mark.smoke
def test_signup():
    print("signup is implemented successfully")
@pytest.mark.low
def test_contact():
    print("contact is implemented successfully")"""

"""@pytest.mark.smoke
def test_login():
    print("login is implemented successfully")
@pytest.mark.smoke
def test_signup():
    print("signup is implemented successfully")
@pytest.mark.low
def test_contact():
    print("contact is implemented successfully")

def test_cart():
    print("cart is implemented successfully")

def test_wishlist():
    print("wishlist is implemented successfully")
    
#pytest -vs -m "not smoke  and not low" markers.py
collected 5 items / 3 deselected / 2 selected

markers.py::test_cart cart is implemented successfully
PASSED
markers.py::test_wishlist wishlist is implemented successfully
PASSED"""

"""@pytest.mark.smoke
def test_login():
    print("login is implemented successfully")
@pytest.mark.sanity
def test_signup():
    print("signup is implemented successfully")
@pytest.mark.low
def test_contact():
    print("contact is implemented successfully")
    
pytest -vs -m "sanity" markers.py
collected 3 items / 2 deselected / 1 selected

markers.py::test_signup signup is implemented successfully
PASSED"""

"""@pytest.mark.smoke
def test_login():
    print("login is implemented successfully")
@pytest.mark.sanity
def test_signup():
    print("signup is implemented successfully")
@pytest.mark.low
def test_contact():
    print("contact is implemented successfully")
    
pytest -vs -m "smoke or low" markers.py 
collected 3 items / 1 deselected / 2 selected

markers.py::test_login login is implemented successfully
PASSED
markers.py::test_contact contact is implemented successfully
PASSED"""

"""#class level
@pytest.mark.smoke
class Testdemo:
    def test_case2(self):
        print("test_case 2 is executing")
    def test_case3(self):
        print("test_case 3 is executing")"""

#Built in Markers:
#skip
"""@pytest.mark.skip
def test_Tc1():
    print("Tc1 is passed")"""

"""@pytest.mark.skip(reason = "not important")
def test_Tc2():
    print("Tc2 is passed")
 """

#skipif
"""tid = 143
@pytest.mark.skipif( tid in [143,443,444],reason = "not part of test suit" )
def test_Tc3():
    print("Tc3 is passed")
Browser = "JE"
@pytest.mark.skipif(Browser in "JE",reason = "not support")
def test_Tc4():
    print("Tc4 is passed")"""

#xfail
"""@pytest.mark.xfail
def test_spam():
    print("test_spam is executed")"""

"""@pytest.mark.xfail
def test_cart():
    print("test_cart is executed"+10)"""

 #pytest -vs markers.py
"""i = 100
@pytest.mark.xfail(i in [200,100,300],reason= "not important")
def test_spam():
    print("test_spam is executed")"""

#parameterized
"""@pytest.mark.parametrize("name",["suhas"])
def test_greet(name):
    print("hi",name)"""

"""@pytest.mark.parametrize("name",["suhas","surya","aniket","ram"])
def test_greet(name):
    print("hi",name)"""

"""@pytest.mark.parametrize("a,b",[[10,20],[30,40],[50,60]])
def test_greet(a,b):
    print(a+b)"""
@pytest.mark.parametrize("name")
def test_greet(name):
    print("hi",name)