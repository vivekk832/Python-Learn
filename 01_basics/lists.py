# >>> tea_varities = ["Black", "Green","Oolong","white"]
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'white']
# >>> print(tea_varities[0])
# Black
# >>> print(tea_varities[-])
#   File "<stdin>", line 1
#     print(tea_varities[-])
#                         ^
# SyntaxError: invalid syntax
# >>> print(tea_varities[-1])
# white
# >>> print(tea_varities[1:3])
# ['Green', 'Oolong']
# >>> print(tea_varities[::1])
# ['Black', 'Green', 'Oolong', 'white']
# >>> print(tea_varities[::2])
# ['Black', 'Oolong']
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'white']
# >>> tea_varities[3] = "Herbal"
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'Herbal']
# >>> tea_varities[1:2]="Lemon"
# >>> tea_varities
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
# >>> tea_varities = ["Black", "Green","Oolong","white"]
# >>> tea_varities[1:2]
# ['Green']
# >>> tea_varities[1:2]=["Lemon"]
# >>> tea_varities
# ['Black', 'Lemon', 'Oolong', 'white']
# >>> tea_varities[1:1]
# []
# >>> tea_varities[1:1]=["test","test"]
# >>> tea_varities
# ['Black', 'test', 'test', 'Lemon', 'Oolong', 'white']
# >>> tea_varities[1:1]=["test","test"]
# >>> tea_varities
# ['Black', 'test', 'test', 'test', 'test', 'Lemon', 'Oolong', 'white']
# >>> tea_varities[1:1]=[]
# >>> tea_varities
# ['Black', 'test', 'test', 'test', 'test', 'Lemon', 'Oolong', 'white']
# >>> tea_varities[1:5]=[]
# >>> tea_varities
# ['Black', 'Lemon', 'Oolong', 'white']
# >>> for tea in tea_varities:
# ...     print(tea)
# ... 
# Black
# Lemon
# Oolong
# white
# >>> for tea in tea_varities:
# ...     print(tea,end=" ")
# ... 
# Black Lemon Oolong white >>> 
# >>> tea_varities
# ['Black', 'Lemon', 'Oolong', 'white']
# >>> if "Oolong" in tea_varities:
# ...     print("i have it ")
# ... 
# i have it 
# >>> tea_varities.append("green")
# >>> tea_varities
# ['Black', 'Lemon', 'Oolong', 'white', 'green']
# >>> tea_varities.pop()
# 'green'
# >>> tea_varities
# ['Black', 'Lemon', 'Oolong', 'white']
# >>> tea_varities.remove("green")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
# >>> tea_varities.insert(1,"Green")
# >>> tea_varities
# ['Black', 'Green', 'Lemon', 'Oolong', 'white']
# >>> tea_varities_copy=tea_varities.copy()
# >>> tea_varities_copy.append("Lemon")
# >>> tea_varities
# ['Black', 'Green', 'Lemon', 'Oolong', 'white']
# >>> tea_varities_copy
# ['Black', 'Green', 'Lemon', 'Oolong', 'white', 'Lemon']
# >>> tea_varities_copy.pop()
# 'Lemon'
# >>> 