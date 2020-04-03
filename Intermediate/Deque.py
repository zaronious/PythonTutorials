from collections import deque

# faster at adding items to the beginning and end of a list

d = deque("hello")

d.append("4")
d.appendleft("5")
print(d)
d.pop()
print(d)
d.popleft()
print(d)
# d.clear()
# print(d)
d.extend("456")
print(d)
d.extend([1, 2, 3])
print(d)
d.extendleft("hey")
print(d)
d.rotate(-2)
print(d)
d.rotate(5)
print(d)

e = deque("hello", maxlen=5)
print(e)
e.append(1)
print(e)
e.extend([1, 2, 3])
print(e)
e.reverse()
print(e)
