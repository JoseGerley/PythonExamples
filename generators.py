from itertools import count
import time

def fibi_gen(max:int=10):
    n1 = 0
    n2 = 1
    counter = 0
    
    while True:
        if counter >= max:
            break
        if counter == 0:    
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1,n2 = n2,aux
            counter += 1
            yield aux

def run():
    fibonacci = fibi_gen()
    for elem in fibonacci:
        print(elem)
        time.sleep(0.5)

if __name__=='__main__':
    run()        