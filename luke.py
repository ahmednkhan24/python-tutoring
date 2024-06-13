  
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

# Step 2: print out the first element of the grades dictionary

# Step 3: grab the command line argument, and print it out
person = sys.argv[1]
print(person)

# Step 4: access the relation of the person
relation = relations[person]

# Step 5: create the message
message = 'Luke, I am your ' + relation

# Step 6: print out the message
print(message)
