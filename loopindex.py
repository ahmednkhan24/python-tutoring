import sys

# Grab the list from the command line 
# Input: `python loopindex.py 1 2 3` -> loop_list = ['1', '2', '3']
loop_list = sys.argv[1:]

def loop_index():
  # loop through every index of loop_list
  # Ex: loop_list = ['1', '2', '3']
  # len(loop_list) = 3
  # range(len(loop_list)) -> loop 3 times, 
  # where `i` = 0 on loop 1
  # where `i` = 1 on loop 2
  # where `i` = 2 on loop 3
  for i in range(len(loop_list)):
    # if loop_list = ['1', '2', '3'], then loop_list[0] = '1', loop_list[1] = '2', etc
    num_str = loop_list[i]

    # convert the string to an integer. 
    # '2' is of type str, but 2 is of type int
    num_int = int(num_str)

    # add the index to the number in the array
    # if loop_list = ['1', '2', '3']
    # where `i` = 0 on loop 1, then 1 + 0 = 1
    # where `i` = 1 on loop 2, then 2 + 1 = 3
    # where `i` = 2 on loop 3, then 3 + 2 = 5
    value = num_int + i

    # add the result to the final array
    print(result)

# invoke the function we defined above
loop_index()
