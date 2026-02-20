def my_decorator(func):
    def wrapper():
        print("before wrapper")
        func()
        print("after wrapper")
    return wrapper

@my_decorator
def fn_test():
    print("hello from fn_test")

fn_test()

# my_decorator(fn_test)()

print("=== ==== ====== ====== =====")

def capitalise_first_letter(fn2):
    def wrapper(*args, **kwargs):
        title = fn2(*args, **kwargs)
        title = title.capitalize()
        return title
    return wrapper

def add_symbol(fn2):
    def wrapper(*args, **kwargs):
        title = fn2(*args, **kwargs)
        if 'end' in kwargs:
            end_s = kwargs['end']
        else:
            end_s = '.'
        if not title.endswith(end_s):
            title += end_s
        return title
    return wrapper

@capitalise_first_letter
@add_symbol
def fn_test2(s, end='.'):
    return s

@capitalise_first_letter
@add_symbol
def fn_test3():
    return "hello from fn_test3"

print(fn_test2('hello from fn_test2', end='!'))
print(fn_test3())


