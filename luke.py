  
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
print(relations)

# Step 2: grab the command line argument, and print it out
person = sys.argv[1]
print(person)

# Step 3: access the relation of the person
relation = relations[person]

# Step 4: create the message
message = 'Luke, I am your ' + relation

# Step 5: print out the message
print(message)
