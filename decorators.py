def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


def logger(func):
    def wrapper(x):
        func(x)
    return wrapper

@logger
def log(x):
    print(x)

log(3)