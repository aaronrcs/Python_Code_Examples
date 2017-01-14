#These are the items in our shoping list
shopping_list = ["pants", "skateboards"]

#dictionary called "stock"
stock = {
    "hoodie": 5,
    "pants": 5,
    "skateboards": 30,
    "Wheels": 10
}

#dictionary called "prices"
prices = {
    "hoodie": 1,
    "pants": 15,
    "skateboards": 35,
    "Wheels": 5
}


#fucntion is made that computes the bill after shopping
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        else:
            return "The item out of stock!"
    return "%s dollars" % total

print("Your total bill: ")
print (compute_bill(shopping_list))