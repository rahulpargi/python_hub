#program to demonstrate encoding
#string to byte

a='hello world'

#intializing byte object
e=b'hello world'

#using encode() to encode the string
d=a.encode('ASCII')

#check whether it is converted or not

if(d==e):
	print('Encoding successful')
else:
	print('Encoding Failed')
