# Created By: Deep Parmar ('deep56parmar@hotmail.com')
# ADT Lists (ALternative of array in python, also called Sequence)

indianStates = ['Gujarat', 'Kerala', 'Rajasthan']
indianStates.append('UP')
indianStates.remove('Kerala')
indianStates.insert(3, 'Assam')
indianStates.sort()
indianStates.append(['Delhi', 'J&K'])
indianStates.append(123)
print(indianStates)

# Functions supporting ADTs are done on the current object.
# It does not create a new object.
# Which is called mutation of the object in python.
# So print(indianStates.sort()) will return None.
# use sorted(indianStates) for getting sorted objects.

listTest = []  # Initialize an emptly list directly
listConstruct = list()  # Initialize the list with constructor

listNum = [1, 2, 3, 4, 0, -1]
# python will understand both are the same object so changes are reflected.
listNumClone = listNum
# Changes won't be reflected coz both are different object.
listNumCopy = list(listNum)
print(listNum is listNumClone)
print(listNum is listNumCopy)
print(listNum == listNumClone)
print(listNum == listNumCopy)
print(listNum, listNumClone, listNumCopy)
listNumClone.reverse()
listNumCopy.sort()
print(listNum, listNumClone, listNumCopy)
