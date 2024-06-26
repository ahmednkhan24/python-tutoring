import sys
import numpy as np

np.random.seed(42)

def really_random(size_str, multiply_str, index_str):
  print(size_str, multiply_str, index_str)
  size = int(size_str)
  multiply = int(multiply_str)
  index = int(index_str)

  if index < size:
    random_numbers = np.random.randint(0, 10, size=size)
    print("random_numbers: ", random_numbers)

    # multiplied = np.multiply(random_numbers, multiply)
    multiplied = random_numbers * multiply
    print('multiplied: ', multiplied)

    result = multiplied[index]
    print("Your random value is", result)


really_random(sys.argv[1], sys.argv[2], sys.argv[3])
