#Using Dictionaries and Lists (Example)

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'hobbies' : ['Video Games','Skateboarding', 'Coding','Tennies']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

#Adding a key 'pocket' and assigning a list to it
inventory['pocket'] = ['seashell','strange berry','lint']

#Sorting the list associated with the key value 'backpack'
inventory['backpack'].sort()

#Using the key 'backpack' to remove 'dagger' from the list
inventory['backpack'].remove('dagger')

#Using the key 'gold' to 50 to 500
inventory['gold'] += 50

print (inventory)