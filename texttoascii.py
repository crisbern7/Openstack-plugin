import math

file = open ('a.txt', "r")
data = file.read()
asci = [ord(c) for c in data]
file.close()
print(asci)

x = len(asci)
print (x)
print(type(x))
n= 0
status = False
print (math.sqrt(x))

'''
if isinstance(math.sqrt(x), int):
    print(Hi)
    status = True
elif isinstance(math.sqrt(x), float):
    status = False
    while status == False:
        n+1
        x+1
        if type(math.sqrt(x)) == int:
            status = True
print(n)
'''

if type(1) == type(math.sqrt(x)):
    print(Hi)
    status = True
elif type(1.1) == type(math.sqrt(x)):
    status = False
    while status == False:
        n=n+1
        x += 1
        if type(math.sqrt(x)) == int:
            status = True
print(n)