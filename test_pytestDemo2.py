

#@pytest.fixture#

import pytest

@pytest.fixture()
def setup():
    print("Once before every method")

def testmethod1(setup):
    print("this ist test method 1")

def testmethod2(setup):
    print("this ist test method 2")

#pytest -v -s C:\Users\manju\PycharmProjects\pythonProject5\pytestDemoPack#to run all modules in pack
#pytet#
#pytest -v -s
#pytest -v -s test_pytestSignup.py#we can run only one module
#pytest -v -s test_pytestSignup.py::test_signupByFacebook#to run perticular method
