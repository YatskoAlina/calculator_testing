import unittest
import time
import math

from calculator_setting import run_calculator
from additional import generate_random_number, get_number, get_sqrt_or_error
from additional import get_numbers_of_symbols, trim_num, contain_digits
from pywinauto.keyboard import send_keys


class TestingFunctions(unittest.TestCase):

    def test_square_root(self):
        dlg = run_calculator()

        # generate int data
        num = generate_random_number(-10000, 10000)

        # generate fractional data
        # num = (generate_random_number(-10000, 10000) / 100)

        str_num = str(num)
        count = len(str_num)
        minus = False

        # enter data
        for i in range(count):
            if str_num[i] == '.':
                dlg.child_window(auto_id='decimalSeparatorButton').click()
            elif str_num[i] == '-':
                minus = True
            else:
                dlg.child_window(auto_id='num{a}Button'.format(a=str_num[i])).click()
            time.sleep(0.25)

        # change to negative/positive
        if minus:
            dlg.child_window(auto_id='negateButton').click()

        # click square root button
        dlg.child_window(auto_id='squareRootButton').click()

        # get result in text form
        result = dlg.child_window(auto_id='CalculatorResults').window_text()

        # check if result contain digits
        if contain_digits(result):
            real_res = get_number(result)
            exp_res = trim_num(get_sqrt_or_error(num), get_numbers_of_symbols(real_res))

            # compare digital result
            self.assertEqual(exp_res, real_res)
        else:
            # checking for error
            self.assertEqual('Display is Invalid input', result)

        time.sleep(1)
        dlg.close()

    def test_quadratic_degree(self):
        dlg = run_calculator()

        # num = (generate_random_number(-10000, 1000) / 100)
        num = generate_random_number(-1000, 1000)
        num_c = str(num).replace('.', ',')
        dlg.type_keys(num_c)
        dlg.child_window(auto_id='negateButton').click()
        send_keys('{ENTER}')

        time.sleep(1)
        dlg.child_window(auto_id='xpower2Button').click()
        result = dlg.child_window(auto_id='CalculatorResults').window_text()
        real_res = get_number(result)

        time.sleep(1)
        exp_res = trim_num(math.pow(-num, 2), get_numbers_of_symbols(real_res))
        self.assertEqual(exp_res, real_res)
        dlg.close()

    def test_invert(self):
        dlg = run_calculator()

        num = (generate_random_number(-10000, 1000) / 100)
        # num = generate_random_number(-1000, 1000)
        num_c = str(num).replace('.', ',')

        # divide to 0
        # num_c = 0

        dlg.type_keys(num_c)
        dlg.child_window(auto_id='negateButton').click()
        send_keys('{ENTER}')

        time.sleep(1)
        dlg.child_window(auto_id='invertButton').click()
        result = dlg.child_window(auto_id='CalculatorResults').window_text()

        if contain_digits(result):
            real_res = get_number(result)
            exp_res = trim_num(1 / (-num), get_numbers_of_symbols(real_res))
        else:
            self.assertEqual('Display is Cannot divide by zero', result)

        time.sleep(1)

        dlg.close()


if __name__ == '__main__':
    unittest.main()
