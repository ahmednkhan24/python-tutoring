import sys

loop_list = sys.argv[1:]

def loop_index():
  result = []
  for i in range(len(loop_list)):
    num_str = loop_list[i]
    num_int = int(num_str)
    value = num_int + i
    result.append(value)
  print(result)

loop_index()
