import sys
import numpy as np

np.random.seed(42)

def really_random(size_str, multiply_str, index_str):
  # convert the strings to integers
  size = int(size_str)
  multiply = int(multiply_str)
  index = int(index_str)

  # don't do anything if the index is beyond the array size, or else the program will crash
  if index < size:
    # create an array of `size` of random numbers between 0 and 10
    random_numbers = np.random.randint(0, 10, size=size)

    multiplied = random_numbers * multiply

    result = multiplied[index]
    print("Your random value is", result)


really_random(sys.argv[1], sys.argv[2], sys.argv[3])
