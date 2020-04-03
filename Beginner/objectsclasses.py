class number:
    def __init__(self, num):
        self.var = num

    def display(self, x):
        print(x)


num = number(23)
num.display(num.var)
num.display(52)
