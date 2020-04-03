# Don't need to import all of collections
# import collections
from collections import Counter

c = Counter("gallad")
print(c)
d = Counter(["a", "b", "c", "d", "b"])
print(d)
e = Counter({"a": 1, "b": 2})
print(e)
f = Counter(cats=4, dogs=7)
print(f["cats"])
# does not return an error like dictionary would, returns 0
print(f["pet"])

# prints every element in the list
print(list(f.elements()))

# prints most common element, number is how many elements to display
print(d.most_common(2))

# subracts number of instances in a list from another
g = Counter(a=4, b=2, c=0, d=-2)
h = Counter(["a", "b", "b", "c"])
g.subtract(h)
print("Subtract: ", g)
# adds number of instances in a list from another
g.update(h)
print("Update: ", g)
# clears counter
# g.clear()
# print("Clear: ", g)

print("Short Add: ", g + h)
# Subtract won't show 0 or less
print("Short Subtract: ", g - h)

# Intersection (minimum above 0 elements in a list)
print("Intersection: ", g & h)

# Union (Max above 0 elements)
print("Union: ", g | h)

# Collections stuff:
# Containers
# - list
# - set
# - dict
# - tuple - inmuttable

# Types
# - Counter
# - deque
# - namedTuple()
# - orderedDict
# - defauldict
