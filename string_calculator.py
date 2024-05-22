
from unittest import TestCase
import re

def add(numbers):
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers_list = re.split(re.escape(delimiter), numbers)

    else:
        numbers_list = re.split(", | \n", numbers)

    total_sum  = sum(int(i) for i in numbers_list)
    return total_sum
