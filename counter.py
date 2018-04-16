from collections import Counter

#with sequence of items
print (Counter(['B','B','A','C']))

#with dictionary
print(Counter({'A':3,'B':5,'C':10}))
#with keyword arguments
print(Counter(A=3,B=7,C=8))

#using Update()
con=Counter()
con.update([1,2,3,1,1,1])
print(con)

#counters can be 0 and negative
c1=Counter(A=4,B=3,C=10)
c2=Counter(A=10,B=3,C=4)
c1.subtract(c2)
print(c1)

#Counting distinct elemets of a list

z=['red','blue','green']
print(Counter(z))
