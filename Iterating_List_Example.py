# I use a "for" to iterate through start_list then append or "add" the values in the start_list squared, to the
#square_list, then sorting the square_list afterwards

start_list = [5, 3, 1, 2, 4]

#Empty list
square_list = []

# Where I interate through the start_list
for x in start_list:
    square_list.append( x ** 2)


square_list.sort()

print ("This is the square_list sorted and squared: ")
print (square_list)
