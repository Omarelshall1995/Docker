#!/bin/python3

valid = True
not_valid = False

print(valid)
print(not_valid)

print(valid==True)
print(not_valid==True)
print(valid != True)
print(not_valid !=False)

print(not valid)
print(not not_valid)
print((10<9) == True)
print((10 == 10) == True )
print(10 >= 9)
print(123 <= 10)
print(bool(0))
print(bool(1))
print(bool(2))
print(1/1)
print(1//1)

x = 10

print(x)

x = x + 1

print(x )

x+=1
print(x)
x-=5
print(x)
x*= 5
print(x)
x/= 5
print(x)

x = 13
print(bin(x))

print(bin(x)[2:].rjust(4,"0"))

print(bin(x >> 1)[2:].rjust(4,"0"))