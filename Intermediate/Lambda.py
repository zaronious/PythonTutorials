# regular function
def func(x):
    return x + 5


print(func(2))

# lambda (anonymous function)
func2 = lambda x: x + 5

print(func2(3))

# lambda within another function
def func3(x):
    func4 = lambda x: x + 5
    return func4(x) + 85


print(func3(5))

func5 = lambda x, y: x + y

print(func5(2, 3))

# with map and filter
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x + 5, a))
print(newList)

newList2 = list(filter(lambda x: x % 2 == 0, a))
print(newList2)
