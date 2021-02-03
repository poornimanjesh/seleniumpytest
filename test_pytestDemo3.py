# @pytest.yeild.fixture()

import pytest


@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every method")


def testmethod1(setup):
    print("This is test method1")


def testmethod2(setup):
    print("This is test method2")

#pytest -v -s C:\Users\manju\PycharmProjects\pythonProject5\pytestDemoPack#to run all modules in pack
#pytet#
#pytest -v -s
#pytest -v -s test_pytestSignup.py#we can run only one module
#pytest -v -s test_pytestSignup.py::test_signupByFacebook#to run perticular method
