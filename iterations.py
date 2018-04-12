cars=['aston','audi','ferrari']
for x in cars:
	print(x)
#indexing using range
a=['apple','grapes','banana']
for i in range(len(a)):
	print(a[i])
#Accessing items using iterate()

for x in enumerate(cars):
	print(x[0],x[1])
#demonstrating the use of start un enumerate
for x in enumerate(cars,start=1):
	print(x[0],x[1])
#looping extensions
#two iterators for  a single looping construct
b=['hello','world','heyaa']
c=['first','second','third']
#single dictionary hold values b and c
d={1:'500',2:'300',3:'400',4:'600',5:'700',6:'900'}
#printing b
for index, e in enumerate(b,start=1):
	print(e,d[index])

#printing c
for index,f in enumerate(c,start=1):
	print(f,d[index+len(b)])

#using zip
first=['hello','world']
second=['how','are']

#combining list and printing
for x,t in zip(first,second):
	print(x,t)

