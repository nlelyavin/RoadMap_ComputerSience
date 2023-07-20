"""Двусторонняя очередь. Можно взаимодействовать с элементом, как сначала списка, так и с конца"""

from collections import deque

# deque
queue = deque([1, 2, 3])

# append
queue.append(4)  # -> None. [1, 2, 3, 4]

# appendleft
queue.appendleft(0)  # -> None. [0, 1, 2, 3, 4]

# popleft
print(queue.popleft())

# pop
print(queue.pop())
