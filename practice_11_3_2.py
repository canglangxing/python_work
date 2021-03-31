import unittest
from practice_11_3_1 import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('Chris', 'Tang', 10000)
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 20000)

if __name__ == '__main__':
    unittest.main()