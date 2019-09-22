# Created By: Deep Parmar ('deep56parmar@hotmail.com')
# Flow Control - Loops (For loops, range() function, while loops)

for i in range(1,20):
    print('i is {}'.format(i), end='\t')

numbers = '1,12,123,321,345,47656,78,97,354,432'
for i in range(0,len(numbers)):
    if numbers[i] in '0123546789':
        print(numbers[i], end='')

for state in ['Gujarat', 'Rajasthan', 'Kashmir', 'Kerala']:
    print('This city is in state ',state)

# range function range(start, stop, steps)
for i in range(0,100,5):
    print(i)
i = 0
while i<10:
    print(i)
    i +=1

a,b = 10,20

print(a,b)

a,b = b,a
print(a,b)