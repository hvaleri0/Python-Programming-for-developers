from array import array

numbers = array('i', [1, 2, 3])

numbers[0] = 1.0  # error because ist a float and not a signed interger
