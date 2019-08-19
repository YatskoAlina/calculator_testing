import random
import math


def get_number(some_str):
    splited_str = some_str.split(" ", 2)
    without_symb = splited_str[2].replace("\xa0", "")
    without_spaces = without_symb.replace(" ", "")
    for_convert = without_spaces.replace(",", ".")
    converted = float(for_convert)
    return converted


def generate_random_number(start, end):
    num = random.randrange(start, end + 1)
    return num


def get_sqrt_or_error(num):
    try:
        d = math.sqrt(num)
        return d
    except:
        return 'Display is Invalid input'


def trim_num(num, count):
    a = round(num, count)
    return a


def contain_digits(sting):
    slp_str = sting.split(' ', 2)[2]
    minus_ex = slp_str.find('-')

    ask = slp_str[0].isdigit() or minus_ex == 0
    if ask:
        return True
    else:
        return False


def get_numbers_of_symbols(num):
    spl_num = str(num).split('.')
    n2 = len(spl_num[1])
    return n2


# -2086 = 70,17121917139533