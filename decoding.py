#program to demonstrate decoding
# byte object to string
a='hello world'

#initializing byte object
c=b'hello world'

#using decode() to decode the byte object

d=c.decode('ASCII')

#check if decoded or not

if (d==a):
	print('decoding successfull')
else:
	print('decoding failed')