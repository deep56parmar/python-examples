# Created By: Deep Parmar ('deep56parmar@hotmail.com')
# Date :  20/07/2018
# Flow Control - Loops (For loops, range() function)

for i in range(1,20):
    print('i is {}'.format(i), end='\t')

numbers = '1,12,123,321,345,47656,78,97,354,432'
for i in range(0,len(numbers)):
    if numbers[i] in '0123546789':
        print(numbers[i], end='')

