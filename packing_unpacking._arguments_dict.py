#dictionary items using **
def fun(a,b,c):
	print(a,b,c)
#a call with unpacking of dictionary
d={'a':1,'b':2,'c':10}
fun(**d)
#packing
def fun(**args):
	print(type(args))

	for i in args:
		print("%s = %s" % (i,args[i]))

fun(name='hello',id='101',lang='python')
