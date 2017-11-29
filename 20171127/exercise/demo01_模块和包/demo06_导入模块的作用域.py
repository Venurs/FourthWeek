from demo01_模块和包.a import n, foo

foo()  # n = 30

n = 1000

print(n)  # n = 1000

foo()  # ?

def test():
    print(n)

test()

foo = test
foo()