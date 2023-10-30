listOfMaterials = ['pen', 'book', 'pencil', 'journal']
print(listOfMaterials)
print(listOfMaterials[1])
print(listOfMaterials[-1])

#change the material in the position[] for the new one
listOfMaterials[2] = 'e-book'
print(listOfMaterials)

listOfMaterials.append('notebook')
print(listOfMaterials)

listOfMaterials.insert(0, 'eraser')
print(listOfMaterials)

del listOfMaterials[0]
print(listOfMaterials)

element = listOfMaterials.pop()
print(element)
print(listOfMaterials)

listOfMaterials.sort()
print(listOfMaterials)

########################################

listOfNumbers = [10, 8, 9, 2, 5]
print(listOfNumbers)

listOfNumbers.append(0)
print(listOfNumbers)

listOfNumbers.insert(1, 1)
print(listOfNumbers)

del listOfNumbers[1]
print(listOfNumbers)

elementNum = listOfNumbers.pop()
print(elementNum)
print(listOfNumbers)

listOfNumbers.sort()
print(listOfNumbers)
