  
import sys

relations = {
  'Darth Vader': 'father',
  'Leia': 'sister',
  'Han': 'brother in law',
  'R2D2': 'droid',
  'Rey': 'Padawan',
  'Tatooine': 'homeworld'
}

# Step 1: print out the relations dictionary
print('STEP 1')
print(relations)

# Step 2: print out the first element of the relations dictionary
print('\nSTEP 2')
print(relations['Darth Vader'])

# Step 3: grab the command line argument of the persons name, and print it out
print('\nSTEP 3')
person = sys.argv[1]
print(person)

# Step 4: access the relation of the person from the dictionary, and print it out
print('\nSTEP 4')
relation = relations[person]
print(relation)

# Step 5: create a variable with the message, and print it out
print('\nSTEP 5')
message = 'Luke, I am your ' + relation
print(message)
