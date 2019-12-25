#!/usr/bin/env python3
import sys

def test_has_double_adjacent_digits(value):
    last_v = value[0]
    for i in range(1, len(value)):
        if value[i] == last_v:
            return True
        last_v = value[i]
    else:
        return False

def test_does_not_decrease(value):
    last_v = value[0]
    for i in range(1, len(value)):
        if value[i] < last_v:
            return False
        last_v = value[i]
    else:
        return True

def test(value):
    return len(value) == 6 and test_has_double_adjacent_digits(value) and test_does_not_decrease(value)

def main(min_value, max_value):
    total = 0
    for value in range(min_value, max_value):
        if test(str(value)):
            total = total + 1
    return total

if __name__=="__main__":
    min_max = sys.argv[1].split("-")
    total = main(int(min_max[0]), int(min_max[1]))
    print(f"Total: {total}")