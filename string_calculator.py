
from unittest import TestCase
import re

def add(numbers):
    if not numbers: return 0
    
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers_list = re.split(re.escape(delimiter), numbers)

    else:
        numbers_list = re.split(", | \n", numbers)
    
    negative_numbers = [int(i) for i in numbers_list if int(i)<0]

    if negative_numbers:
        raise ValueError("No negatives allowed")

    total_sum  = sum(int(i) for i in numbers_list )
    return total_sum
