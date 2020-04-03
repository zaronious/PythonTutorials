loop = True


def func():
    global loop
    loop = 7


func()
print(loop)
