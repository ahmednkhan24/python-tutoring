import sys

grades = {
  'Biology': 80,
  'Physics': 88,
  'Chemistry': 98,
  'Math': 89,
  'English': 79,
  'Music': 67,
  'History': 68,
  'Art': 53,
  'Economics': 95,
  'Psychology': 88
}

# Step 0: Define average and how to calculate it
# https://www.youtube.com/watch?v=95h7qAkz5QY&ab_channel=ehow

# Step 1: print out the grades dictionary
print('STEP 1')
print(grades)

# Step 2: print out the first element of the grades dictionary
print('\nSTEP 2')
print(grades['Biology'])

# Step 3: loop through all of the subjects and print them out
print('\nSTEP 3')
for subject in grades:
    print(subject)

# Step 4: loop through all subjects and print out the grade for the subject
print('\nSTEP 4')
for subject in grades:
    print(grades[subject])

# Step 5: grab the command line argument for the subjectToExclude, and print it out
print('\nSTEP 5')
subjectToExclude = sys.argv[1]
print(subjectToExclude)

# Step 6: print out the grade value of the subjectToExclude
print('\nSTEP 6')
print(grades[subjectToExclude])

# Step 7: loop through all subjects and print them out, except for subjectToExclude
print('\nSTEP 7')
for subject in grades:
  if subject != subjectToExclude:
     print(subject)

# Step 8: loop through all subjects and print out the grade, except for subjectToExclude
print('\nSTEP 8')
for subject in grades:
  if subject != subjectToExclude:
     print(grades[subject])

# Step 9: initialize the total of all grade values we want to calculate, and print it out
print('\nSTEP 9')
total = 0.00
print(total)

# Step 10: loop through all subjects, add the grade to the total, except for subjectToExclude
print('\nSTEP 10')
for subject in grades:
  if subject != subjectToExclude:
    total = total + grades[subject]
print(total)


# Step 11: calculate the length of the grades dictionary, except for subjectToExclude
print('\nSTEP 11')
length = len(grades) - 1
print(length)

# Step 12: calculate the average of all grades, not including the subjectToExclude
print('\nSTEP 12')
average = total / length
print(average)

# Step 13: round the average to 2 decimals
print('\nSTEP 13')
rounded = round(average, 2)
print(rounded)
