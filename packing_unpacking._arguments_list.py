def fun1(a,b,c):
	print(a,b,c)
#packing arguments to *args
def fun2(*args):
	#convert to list so it can be modified
	args=list(args)
	#modifying args
	args[0]='First'
	args[1]='second'
	#unpacking args 
	fun1(*args)
fun2('hello','from','python')

