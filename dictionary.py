fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-' * 40)
#while True:
#    dict_key = input("Please enter a fruit:")
#    if dict_key == "quit":
#        break    
#    if dict_key in fruit:
#        description = fruit.get(dict_key)
#        print(description)
#    else:
#        print("We don't have a " + dict_key)
