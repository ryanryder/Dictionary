fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple":"round and crunchy"}
#Playing with adding and edting dictionary values.
#print(fruit)
#print(fruit["lemon"])
#fruit["pear"] = "an odd shaped apple"
#print(fruit)
#fruit["lime"] = "great with tequila"
#print(fruit)
#del fruit["lemon"]
print(fruit)
while True:
    dict_key = input("Please enter a fruit:")
    if dict_key == "quit":
        break
    #default value if there is nothing in the dictionary will be send an error message.
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)
    #if dict_key in fruit:
    #    description = fruit.get(dict_key)
    #    print(description)
    #else:
    #    print("We don't have a " + dict_key)