import math
import random
import time

def sumseries(a, b):
    if a<=1:
        return b(1)
    return b(1) + sumseries(a-1, b)	
print(sumseries(200, lambda x: x+1))

def randomthreeminutes():
    elapsed = 0
    letters = [chr(value) for value in range(97, 123)]
    lst = []
    while elapsed < 180:
        sleepsecs = random.randrange(1, 10)
        #print(sleepsecs, elapsed)
        time.sleep(sleepsecs)
        letter = letters[random.randrange(0, 26)]
        lst.append(letter)
        print(letter)
        elapsed += sleepsecs
    return lst
#a = randomthreeminutes()
#print(a)
#print([i for i in a if not time.sleep(1)])

def badsongs():
    return random.randrange(1, 60)
#print(badsongs())