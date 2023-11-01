numbers = list(range(1,11))
print(numbers)

for value in numbers:
    print(value)

square = []

for item in range(1,11):
    squareResult = item ** 2
    square.append(squareResult)

print(square)

print(min(square))
print(max(square))
print(sum(square))

print(numbers[:3])

num = [1, 2, 3, 4]
print(num)
numCopy = num #points to the same memory space
numCopy.append(100)
print(num)
print(numCopy)

num2 = [1,2,3,4]
print(num2)
numCopy2 = num2[:] #copy only elements to create other list
numCopy2.append(500)
print(num2)
print(numCopy2)