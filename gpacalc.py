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
print('STEP 1')
print(gpa_dict)

# Step 2: print out the first element of the grades dictionary
print('\nSTEP 2')
print(gpa_dict['A'])

# Step 3: loop through all of the grade letters and print them out
print('\nSTEP 3')
for letter_grade in gpa_dict:
    print(letter_grade)

# Step 4: loop through all of the grade weights and print them out
print('\nSTEP 4')
for letter_grade in gpa_dict:
    print(gpa_dict[letter_grade])

# Step 5: grab the first command line argument for a letter grade, and print it out
print('\nSTEP 5')
grade1 = sys.argv[1]
print(grade1)

# Step 6: turn the first letter grade into upper case, and print it out
print('\nSTEP 6')
grade1 = grade1.upper()
print(grade1)

# Step 7: access the weight of the grade, and print it out
print('\nSTEP 7')
grade1_weight = gpa_dict[grade1]
print(grade1_weight)

# Step 8: grab the other 3 grades from the command line, make them upper case, and print them out
print('\nSTEP 8')
grade2 = sys.argv[2].upper()
grade3 = sys.argv[3].upper()
grade4 = sys.argv[4].upper()

print(grade2)
print(grade3)
print(grade4)

# Step 9: access the weights of each grade, and print them out
print('\nSTEP 9')
grade2_weight = gpa_dict[grade2]
grade3_weight = gpa_dict[grade3]
grade4_weight = gpa_dict[grade4]

print(grade2_weight)
print(grade3_weight)
print(grade4_weight)

# Step 10: total all of the weights, and print it out
print('\nSTEP 10')
total = grade1_weight + grade2_weight + grade3_weight + grade4_weight
print(total)

# Step 11: calculate the average (GPA) of the total, and print it out
print('\nSTEP 11')
gpa = total / 4
print(gpa)

# Step 12: round the average to 2 decimals
print('\nSTEP 12')
rounded_gpa = round(gpa, 2)
print(rounded_gpa)


# ------------------------------------------------------------------------------
# Challenge, can you do all of that in one function?
def optimal_solution(num_grades_to_grab):
  total = 0.00
  for i in range(num_grades_to_grab):
    grade = sys.argv[i+1].upper()
    weight = gpa_dict[grade]
    total = total + weight
  return round(total / num_grades_to_grab, 2)

# print(optimal_solution(4))

