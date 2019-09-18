# Created By: Deep Parmar ('deep56parmar@hotmail.com')
# Continue , Break keywords

# Continue is used for skipping iteration. 
shoppingList = ['milk', 'honey', 'sugar', 'eggs', 'cake']

for item in shoppingList:
    if item == 'sugar':
        continue
    print(item)

# Break is used for breaking out from iteration

for item in shoppingList:
    if item == 'eggs':
        break
    print(item)

"""
Augmented assignment: 
in iteration if we do a = b + 1 , then python create a variable each time 
then assign its value. To make it more faster and change directly in value 
of current one time variable python support using augmented assignment via
short hand operators. 
 """