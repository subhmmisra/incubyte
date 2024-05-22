
from unittest import TestCase
import re

def add(numbers):
    numbers_list = re.split(", | \n", numbers)
    #numbers_list = numbers.split(',')
    # add \n

    total_sum  = sum(int(i) for i in numbers_list)
    return total_sum

print(add("1, 2, 4"))



