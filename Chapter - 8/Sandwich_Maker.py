import pyinputplus as py

prices = {'wheat': 2, 'white': 1, 'sour dough': 3, 'chicken': 2, 'turkey': 3, 'ham': 2, 'tofu': 1,'cheddar': 1, 'swiss': 2, 'mozzarella': 3, 'mayo': 1, 'mustard': 1, 'lettuce': 1,'ketchup': 1}

print("Prices of all the items: \n",prices,"\n")

e_list=[]
cost=0


bread = py.inputMenu(['wheat','white', 'brown', 'sourdough'], prompt="What type of bread would you like ?\n", numbered=True)
e_list.append(bread)

protein=py.inputMenu(['chicken','turkey','ham','tofu'],prompt="What type of protein would you like ?\n", numbered=True)
e_list.append(protein)

cheese="Do you want cheese on your sandwich ?\n"
cheese_ans=py.inputYesNo(cheese)

if cheese_ans=='yes':
    cheese_type=py.inputMenu(['cheddar','swiss','mozzarella'],prompt="Then what type of cheese would you like ?\n", numbered=True)
    e_list.append(cheese_type)
else:
    print("You don't want to add cheese")

extras="Do you want some extras on your sandwich ?\n"
extras_ans=py.inputYesNo(extras)

if extras_ans=='yes':
    extras_type=py.inputMenu(['mayo','mustard','lettuce','tomato'],prompt="Then what type of extras would you like ?\n", numbered=True)
    e_list.append(extras_type)
else:
    print("You don't want to add any extras")

total_sandwich=py.inputNum('Enter number of sandwiches: ', min=1)


for i in e_list:
    if i in prices:
        cost=cost+prices[i]
print(cost*total_sandwich)
        
