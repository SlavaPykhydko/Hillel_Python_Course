
def fn_outer(param):
    def inner():
        print(param)
    return inner

f = fn_outer("Test")
f()

fn_outer("Test2")()


def counter(start=0):
    def update_counter():
        nonlocal start
        start += 1
        return start
    return update_counter

counter1 = counter(10)
counter2 = counter(20)
print(counter1())
print(counter1())
print(counter1())
print(counter2())
print(counter2())
print(counter2())

def outer(param1):
    def inner(param2):
        print(param1, param2)
    return inner

outer("Slava1")("Slava2")
