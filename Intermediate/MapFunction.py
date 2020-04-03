#
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x ** x


def func2(x):
    return 5


# list converts the map into a list, for readability (double parenthesis):
newList = list((map(func, li)))
print(newList)
newList2 = map(func2, newList)
print(newList2)
newList3 = list((map(func, newList2)))
print(newList3)
