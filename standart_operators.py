import unittest

from pywinauto.keyboard import send_keys
from additional import get_number, generate_random_number
from calculator_setting import run_calculator
import time


class TestingOperators(unittest.TestCase):

    def test_subtraction(self):
        dlg = run_calculator()  # run a program
        # enter data
        for i in range(4):
            num1 = generate_random_number(10, 29)
            num2 = generate_random_number(1, 9)
            dlg.type_keys(num1)
            dlg.type_keys('-')
            time.sleep(1)
            dlg.type_keys(num2)
            time.sleep(1)
            dlg.type_keys('=')
            real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())  # get results
            self.assertEqual(real_res, num1 - num2)  # compare results
            send_keys('{ESC}')
            time.sleep(1)

        dlg.close()

    def test_addition(self):
        num = generate_random_number(1, 9)
        dlg = run_calculator()  # run a program
        # enter data
        dlg.child_window(auto_id='num9Button').click()
        dlg.child_window(auto_id='plusButton').click()
        dlg.type_keys(num)
        dlg.child_window(auto_id='equalButton').click()
        real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())  # get results
        self.assertEqual(real_res, 9 + num)  # compare results
        dlg.close()

    def test_division(self):
        num = generate_random_number(-100, 100)
        dlg = run_calculator()  # run a program
        # enter data
        dlg.type_keys(num)
        dlg.child_window(auto_id='divideButton').click()
        dlg.child_window(auto_id='num8Button').click()
        time.sleep(1.5)
        send_keys('{ENTER}')
        time.sleep(1.5)
        real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())  # get results
        self.assertEqual(real_res, num / 8)  # compare results
        dlg.close()

    def test_multiplication(self):
        dlg = run_calculator()  # run a program
        # enter data
        dlg.child_window(auto_id='num7Button').click()
        dlg.child_window(auto_id='multiplyButton').click()

        num = generate_random_number(0, 200)
        str_num = str(num)
        count = len(str_num)

        for i in range(count):
            dlg.child_window(auto_id='num{a}Button'.format(a=str_num[i])).click()
            time.sleep(0.5)

        dlg.child_window(auto_id='equalButton').click()
        real_res = get_number(dlg.child_window(auto_id='CalculatorResults').window_text())  # get results
        self.assertEqual(real_res, 7 * num)  # compare results
        time.sleep(1)
        dlg.close()


if __name__ == '__main__':
    unittest.main()
