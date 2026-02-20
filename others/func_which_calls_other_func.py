def f1():
    print("hello from f1")

def f2(func):
    print("hello from f2")
    func()

f2(f1)

def f3():
    print("hello from f3")

f4 = f3
f4()