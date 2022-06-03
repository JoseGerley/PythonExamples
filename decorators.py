from datetime import datetime
import re
import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        print("Inicio de tiempo")
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        time_elapsed = end - start
        print('Execution time {} s'.format(time_elapsed.total_seconds()))
        return result
    return wrapper

def print_saludo(func):
    def wrapper(*args, **kwargs):
        print('Hola')
        func(*args, **kwargs)
    return wrapper

@execution_time
def random_func():
    for _ in range(1000000):
        pass

@execution_time
@print_saludo
def suma(a:int,b:int)->int:
    print (a + b)


suma(10,20)