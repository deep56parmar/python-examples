# Created By: Deep Parmar ('deep56parmar@hotmail.com')
# Date :  20/07/2018
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