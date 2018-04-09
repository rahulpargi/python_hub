#case 1 - Immutable Target
print('Immutable Target:')
import operator

#initialize value

x=5
y=6
a=7
d=2

#using add() to add the arguments passed
z=operator.add(a,d)
#using iadd() to add the arguments
q=operator.iadd(x,y)
#printing the modified values
print("value using normal operator:",end="")
print(z)
#printing using modified value
print("value using inplace operator:",end="")
print(q)
#printing value of first argument, value is unchanged
print("value of first argument using normal operator:",end="")
print(a)
#printing value of first argument,value is unchanged
print("value of first argument using inplace operator:",end="")
print(x)

#case - 2 Mutable Target
print('Mutable Target:')
#initializing list
a=[1,2,3,4]
#using add() to add the arguments passed
z=operator.add(a,[1,2,3])

#printing the modifed values
print('value using normal operator:',end="")
print(z)
#printing value of first argument,value is unchanged
print('value of first argument using normal operator:',end="")
print(a)

#using iadd() to add the arguments the arguments passed
p=operator.iadd(a,[1,2,3])

#printing the modified values
print('value after using inplace operator:',end="")
print(p)

#printing value of first argument,value is changed
print("value of first argument using inplace operator:",end="")
print(a)
