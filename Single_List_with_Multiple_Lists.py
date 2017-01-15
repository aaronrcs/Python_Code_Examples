#List Contains two sublists inside this single list
numbers = [[1, 2, 3], [4, 5, 6, 7]]


# This function iterates over a single list containing multiple lists
def print_List(lists):
    results = []
    for numbers in lists:
        for item in numbers:
            results.append(item)

    return results

print("List: ")
print (print_List(numbers))