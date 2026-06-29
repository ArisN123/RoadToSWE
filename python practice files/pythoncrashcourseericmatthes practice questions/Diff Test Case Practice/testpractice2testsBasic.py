from testpractice2 import Employee
import unittest

class TestEmployee(unittest.TestCase):
    """ test case for employee class"""
    def test_give_default_raise(self):
        employeefortest = Employee('aris','niamonitakis',20000)
        employeefortest.give_raise()
        self.assertEqual(employeefortest.salary, 25000)

    def test_give_custom_raise(self):
        employeefortest = Employee('aris','niamonitakis',20000)
        employeefortest.give_raise(20000)
        self.assertEqual(employeefortest.salary,40000)

unittest.main()