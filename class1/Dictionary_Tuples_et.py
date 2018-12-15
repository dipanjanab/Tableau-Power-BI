fruits = { "orange" : "A sweet and sour fruit",
           "apple": "good for health",
           "leamon": "has vitanin C in it ",
           "carrot": "Used as a salad",
           "carrot": "Can be used in many side dishes",
           "mango": "Best summer fruit"}


key= input("Enter fruit you want to search: ")
print(fruits[key])
#fruits["mango"] = "Seasonal fruit , very popular"


#print(fruits)

#looping on a dictionary
for key in fruits:
    print("{} :{}".format(key,fruits[key]))

#looping on values , not very efficient
for value in fruits.values():
    print(value)