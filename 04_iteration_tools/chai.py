import time 
print("chai is here "
      )
username = "hitesh"
print(username)


# @vivekk832 ➜ /workspaces/Python-Learn/04_iteration_tools (main) $ ls
# chai.py  chaipy
# @vivekk832 ➜ /workspaces/Python-Learn/04_iteration_tools (main) $ python3
# Python 3.12.5 (main, Aug 13 2024, 02:17:09) [GCC 10.2.1 20210110] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> open('chai.py')
# <_io.TextIOWrapper name='chai.py' mode='r' encoding='UTF-8'>
# >>> f=open('chai.py')
# >>> f.readline()
# 'import time \n'
# >>> f.readline()
# 'print("chai is here "\n'
# >>> f.readline()
# '      )\n'
# >>> f.readline()
# 'username = "hitesh"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>> f=open('chai.py')
# >>> f.__next__()
# 'import time \n'
# >>> f.__next__()
# 'print("chai is here "\n'
# >>> f.__next__()
# '      )\n'
# >>> f.__next__()
# 'username = "hitesh"\n'
# >>> f.__next__()
# 'print(username)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> 
# >>> for line in open('chai.py'):
# ... print(line)
#   File "<stdin>", line 2
#     print(line)
#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for line in open('chai.py'):
# ...     print(line)
# ... 
# import time 

# print("chai is here "

#       )

# username = "hitesh"

# print(username)
# >>> for line in open('chai.py'):
# ... 
#   File "<stdin>", line 2
    
#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> f=open('chai.py')
# >>> while Ture:
# ...     line =f.readline()
# ...     if not line:break
# ...     print(line , end=" ")
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Ture' is not defined
# >>> while True:
# ...     line =f.readline()
# ...     print(line , end=" ")
# ...     line =f.readline()
# ...     print(line , end=" ")
# ...     if not line:break
# ...     print(line , end=" ")
# ... 
# import time 
#  print("chai is here "
#  print("chai is here "
#        )
#  username = "hitesh"
#  username = "hitesh"
#  print(username)  >>> 
# >>> test = "hitesh"
# >>> if not test:
# ...     print("chai")
# ... 
# >>> 
# >>> 
# >>> myList = [1,2,3,4]
# >>> I = iter(myList)
# >>> I
# <list_iterator object at 0x7e4eafcc1000>
# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> 
# >>> f = open('chai.py')
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__()
# True
# >>> D = {'a':1,'b':2}
# >>> for key in D.keys():
# ...     print(key)
# ... 
# a
# b
# >>> I = iter(D)
# >>> I
# <dict_keyiterator object at 0x7e4eafe73290>
# >>> next(I)
# 'a'
# >>> 
# >>> 
# >>> 
# >>> range(5)
# range(0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> 
# >>> I = iter(R)
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> 