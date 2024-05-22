
from unittest import TestCase
import re

def add(numbers):
    numbers_list = re.split(", | \n", numbers)
    total_sum  = sum(int(i) for i in numbers_list)
    return total_sum



