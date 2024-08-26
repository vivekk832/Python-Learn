# Object Types/ Data Types

# Numbers : 1234, 3.14, 3+4j, 0b111, Decimal(), Fraction()
# String : 'spam', "bob's", b'a\x01c', u'sp\xc4m'
# List : [1,[2,'three'],4.5],list(range(10))
# Tuple :(1,'spam',4,'U'),tuple('spam'),namedtuple
# Dictonary : {'food':'spam','taste':'yum'} , dict(hour=10)
# Set : set('abc'),{'a','b','c'}
# []-brackets   () - parenthesis {}-braces

# File- open('eggs.txt'),open(r'C:\ham.bin','wb')
# Boolean : True , False
# None : None
# Functoins , modules , classes
# Advance : Decoraters , Generators,Iterators,MetaProgamming


# >>> username="chaiaurcode"
# >>> username[0]
# 'c'
# >>> username[0] ="a"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> username[-1]
# 'e'
# >>> 


# to know all methods for attribute
# >>> dir(username)


# list
# >>> mylist = [123, "chai" , 3.14]
# >>> mylist
# [123, 'chai', 3.14]
# >>> len(mylist)
# 3
# >>> mylist[0]
# 123

# dictionaries
# >>> myD= { 'one':'lemon','two':'ginger','god':'virat kohli'}
# >>> myD[one]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'one' is not defined. Did you mean: 'None'?
# >>> myD['one']
# 'lemon'


# Tuples
# >>> myTup = (1,2,3)
# >>> myTup[0]
# 1
# >>> len(myTup)
# 3

# python dosent have any data type as you never assign data type to variable
# but the reference in the memory has a data type which is assigned inside

# List --internal working
# >>> l1=[1,2,3]
# >>> l2=l1
# >>> l1
# [1, 2, 3]
# >>> l2
# [1, 2, 3]
# >>> l1[0]=44
# >>> l1
# [44, 2, 3]
# >>> l2
# [44, 2, 3]
# >>> p1=[1,2,3]
# >>> p2=p1
# >>> p2=[1,2,3]
# >>> p1[0]=45
# >>> p1
# [45, 2, 3]
# >>> p2
# [1, 2, 3]
# >>> 


# >>> h1 = [1,2,3]
# >>> h2 = h1[:]    //slicing
# >>> h2
# [1, 2, 3]
# >>> h1[0] = 65
# >>> h1
# [65, 2, 3]
# >>> h2
# [1, 2, 3]

# >>> n=[1,2,3]
# >>> n
# [1, 2, 3]
# >>> m=n
# >>> m
# [1, 2, 3]
# >>> n
# [1, 2, 3]
# >>> m==n
# True          //Objects are same
# >>> m is n 
# True          //References are same 
# >>> n=m[:]
# >>> m==n
# True          //here still the Objects are same
# >>> m is n 
# False         //References are different
# >>> 