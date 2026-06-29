from testpractice2 import Employee
import unittest

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_4_test = Employee('aris','niamonitakis',20000)

    def test_give_default_raise(self):
        self.employee_4_test.give_raise()
        self.assertEqual(self.employee_4_test.salary, 25000)

    def test_give_custom_raise(self):
        self.employee_4_test.give_raise(20000)
        self.assertEqual(self.employee_4_test.salary,40000)

unittest.main()