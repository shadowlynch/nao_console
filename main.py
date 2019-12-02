from time import time


def decorator(func):
    def wrapper():
        time1 = time()
        func()
        print "the total time for function call is " + str((time() - time1))
    return wrapper


@decorator
def contra():
    for x in range(100000000):
        print x**2


if __name__ == '__main__':
    contra()