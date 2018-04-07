#any data type to int

s='1111'

#printing string conversion to float

c=int(s,2)
print(c)

#char to int
s='4'
c=ord(s)
print(c)

#int to  hexadecimal
c=hex(56)
print(c)

#int to octal
c=oct(56)
print(c)

s='hello'
#string to tuple
c=tuple(s)
print(s)
#string to set
c=set(s)
print(c)
#string to list
c=list(s)
print(c)

a=1
b=2

tup=(('a',1),('f',2),('g',3))
#int to complex numbers
c=complex(1,2)
print(c)
#int to string
c=str(a)
print(c)
#tuple to expression dictionary
c=dict(tup)
print(c)