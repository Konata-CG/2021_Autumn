example = [(1, 2), (3, 4), (5, 6)]
for index, (a, b) in enumerate(example, 1):
    print(index, (a, b), end=" ")

def add(x):
    def addX(y):
        return y + x
    return addX
foo = add(1)
goo = add(-1) 
print(foo(2),end=" ")
print(goo(3))

