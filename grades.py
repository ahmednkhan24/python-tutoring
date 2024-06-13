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
print(grades)

# Step 2: print out the first element of the grades dictionary

# Step 3: grab the command line argument, and print it out
subjectToExclude = sys.argv[1]
print(subjectToExclude)

# Step 4: print out the grade value of the subjectToExclude
print(grades[subjectToExclude])

# Step 6: initialize the total value we want to calculate
total = 0.00

# Step 5: loop through all of the grades and print them out
for subject in grades:
  # Step 8: don't include the subjectToExclude
  if subject != subjectToExclude:
    # Step 7: keep track of the total of all grades
    total = total + grades[subject]

# Step 9: print out the total
print(total)

# Step 10: calculate the length of the grades dictionary
length = len(grades) - 1
print(length)

# Step 11: calculate the average of all grades, not including the subjectToExclude
average = total / length
print(average)

# Step 12: round the average to 2 decimals
rounded = round(average, 2)
print(rounded)
