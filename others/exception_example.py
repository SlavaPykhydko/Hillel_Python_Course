
i = 0

while True:
    try:
        num = int(input("Enter a number > 0: "))
        res = 100 / num
        if num == 100:
            raise NameError("Test Error")
    except ZeroDivisionError:
        print("Division by zero")
    except ValueError:
        print("Incorrect input")
    except TypeError:
        print("Incorrect input 2")
    except:
        print("Something went wrong")
    else:
        print(res)
        break
    finally:
        print("this block works in any case")
        i += 1
        print(f'Count: {i}')

