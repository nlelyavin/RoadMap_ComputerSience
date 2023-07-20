"""Array - Множество. В языке Python представлено ключевым словом list - список"""

"""Default methods"""

# init
array_1 = list()  # -> []
array_2 = list()

# append
array_1.append(1)  # -> None. [1]
array_2.append(2)

# extend
array_1.extend(array_2)  # -> None. [1, 2]

# insert
array_1.insert(1, 5)  # -> None. [1, 5, 2]

# remove
array_1.remove(5)  # -> None. [1, 2]

# pop
array_1.append(25)
array_1.pop()  # -> 25. [1, 2]

# clear
array_2.clear()  # -> None
del array_2[:]  # -> None

# count - Сколько раз встретился элемент
array_1.count(1)  # -> 1

# reverse
array_1.reverse()  # -> None

# index
array_1.index(1)  # -> 0

# sort
array_1.sort(key=lambda x: x, reverse=True)  # -> None. [2, 1]

# copy
array_3 = array_1.copy()  # -> [2, 1]
array_4 = array_1[:]

"""List Comprehensions"""
# 1.
squares = []
for x in range(100):
    squares.append(x ** 2)

print(squares)

# 2
squares = [i ** 2 for i in range(100)]
print(squares)

# 3
squares = list(map(lambda i: i ** 2, range(100)))
print(squares)
