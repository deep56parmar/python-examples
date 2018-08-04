# Created By: Deep Parmar ('deep56parmar@hotmail.com')
# Date :  20/07/2018
# Flow Control - Conditions (if , elif, else)
name = input('Please enter your name: ')
age = int(input('How old are you, {0} ? '.format(name)))
print(age)
if age >= 18:
    print("You are an adult..!")
    if age >= 18 and age <= 30:
        print('You are Young')
    elif age >=30 and age <= 100:
        print('You are getting old or may be already old') 
    else:
        print('Are you some kind of vampire or immortal being? ')
elif age >10 and age <18:
    print('You will be an adult in no time..')
else:
    print('You are still {0} years to go....'.format(18-age))