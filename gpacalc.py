import sys

gpa_dict = {
  'A': 4.0,
  'A-': 3.66,
  'B+': 3.33,
  'B': 3.0,
  'B-': 2.66,
  'C+': 2.33,
  'C': 2.0,
  'C-': 1.66,
  'D+': 1.33,
  'D': 1.00,
  'D-': 0.66,
  'F': 0.00,
}

# Step 0: Define GPA and how to calculate it
# https://www.youtube.com/shorts/YeWTD8ftKpE

# Step 1: print out the gpa dictionary
print(gpa_dict)

# Step 2: print out the first element of the grades dictionary
print(gpa_dict['A'])

# Step 3: grab the first command line argument, and print it out
grade1 = sys.argv[1]
print(grade1)

# Step 4: access the weight regardless of casing, and print it out
grade1 = grade1.upper()
print(grade1)

# Step 5: access the weight of the grade
grade1Weight = gpa_dict[grade1]
print(grade1Weight)

# Step 6: grab the other 3 grades from the command line, 
# regardless of casing, and print them out
grade2 = sys.argv[2].upper()
grade3 = sys.argv[3].upper()
grade4 = sys.argv[4].upper()

print(grade2)
print(grade3)
print(grade4)

# Step 6: access the weights of each grade, and print them out
grade2Weight = gpa_dict[grade2]
grade3Weight = gpa_dict[grade3]
grade4Weight = gpa_dict[grade4]

print(grade2Weight)
print(grade3Weight)
print(grade4Weight)

# Step 6: total the weights, and print it out
total = grade1Weight + grade2Weight + grade3Weight + grade4Weight
print(total)

# Step 7: calculate the GPA (average), and print it out
gpa = total / 4
print(gpa)

# Step 8: round the average to 2 decimals
roundedGpa = round(gpa, 2)
print(roundedGpa)
print()

# ------------------------------------------------------------------------------
# Challenge, can you simplify this by using custom functions?
def grab_x_grades_from_args(num_grades_to_grab):
  grades = []
  for i in range(num_grades_to_grab):
    grades.append(sys.argv[i+1].upper())
  return grades

grades = grab_x_grades_from_args(4)
print(grades)

def grab_weights_of_grades(grades):
  weights = []
  for grade in grades:
    weights.append(gpa_dict[grade])
  return weights

weights = grab_weights_of_grades(grades)
print(weights)

def calculate_average(arr):
  total = 0.00
  for i in arr:
    total = total + i
  return round(total / len(arr), 2)

print(calculate_average(weights))
print()

# ------------------------------------------------------------------------------
# Challenge, can you do all of that in one function?
def optimal_solution(num_grades_to_grab):
  total = 0.00
  for i in range(num_grades_to_grab):
    grade = sys.argv[i+1].upper()
    weight = gpa_dict[grade]
    total = total + weight
  return round(total / num_grades_to_grab, 2)

print(optimal_solution(4))

