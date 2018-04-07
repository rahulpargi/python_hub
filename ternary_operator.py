# 1.simple method
a,b=10,20
min=a if a<b else b
print(min)

# 2.direct method
a,b=10,20
#tuple for selecting a item
print((b,a)[a<b])

#dictionary for selecting an item
print({True:a,False:b}[a<b])

#lambda
print((lambda:b,lambda:a)[a<b]())

# 3.using nested if else
print('both a and b are equal'if a==b else 'a is greater than b' if a>b else 'b is greater than a')