# >>> chai = "masala Chai"
# >>> print(chai)
# masala Chai
# >>> first_char = chai[0]
# >>> print(first_char)
# m
# >>> slice_chai = chai[0:6]
# >>> print(slice_chai)
# masala
# >>> num_list = "0123456789"
# >>> num_list = [:]
#   File "<stdin>", line 1
#     num_list = [:]
#                 ^
# SyntaxError: invalid syntax
# >>> num_list[:]
# '0123456789'
# >>> num_list[:7]
# '0123456'
# >>> num_list[2:]
# '23456789'
# >>> num_list[::2]
# '02468'
# >>> num_list[::3]
# '0369'
# >>> num_list[::-1]
# '9876543210'
# >>> chai
# 'masala Chai'
# >>> print(chai.lower())
# masala chai
# >>> print(chai.upper())
# MASALA CHAI
# >>> chai = "     masala chai     "
# >>> print(chai)
#      masala chai     
# >>> print(chai.strip())
# masala chai
# >>> chai = "lemon chai"
# >>> print(chai.replace("lemon","Ginger"))
# Ginger chai
# >>> chai
# 'lemon chai'
# >>> chai = "Lemon , Ginger,Masala,Mint"
# >>> print(chai.split())
# ['Lemon', ',', 'Ginger,Masala,Mint']
# >>> print(chai.split(", "))
# ['Lemon ', 'Ginger,Masala,Mint']
# >>> chai = "Lemon Ginger,Masala,Mint"
# >>> print(chai.split())
# ['Lemon', ',', 'Ginger,Masala,Mint']
# >>> print(chai.split(", "))
# ['Lemon ', 'Ginger,Masala,Mint']
# >>> 
# >>> chai="masala chai"
# >>> print(chai.find("chai"))
# 7
# >>> print(chai.find("Chai"))
# -1
# >>> chai = "masala chai chai chai"
# >>> print(chai.count("chai"))
# 3
# >>> chai_type = "Masala"
# >>> qunatity =2 
# >>> order = "I ordered {} cups of {} chai"
# >>> 
# >>> order
# 'I ordered {} cups of {} chai'
# >>> print(order.format(quantity,chai_type))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'quantity' is not defined. Did you mean: 'qunatity'?
# >>> print(order.format(qunatity,chai_type))
# I ordered 2 cups of Masala chai
# >>> chai_variety = ["lemon","Masala","Ginger"]
# >>> print(chai_variety)
# ['lemon', 'Masala', 'Ginger']
# >>> print("".join(chai_variety))
# lemonMasalaGinger
# >>> print(" ".join(chai_variety))
# lemon Masala Ginger
# >>> print(" - ".join(chai_variety))
# lemon - Masala - Ginger
# >>> print(" , ".join(chai_variety))
# lemon , Masala , Ginger
# >>> chai = "Masala chai"
# >>> chai 
# 'Masala chai'
# >>> print(len(chai))
# 11
# >>> chia
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'chia' is not defined
# >>> chai
# 'Masala chai'
# >>> for letter in chai :
# ... print (letter)
#   File "<stdin>", line 2
#     print (letter)
#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> 
# >>> for letter in chai :
# ...     print(letter)
# ... 
# M
# a
# s
# a
# l
# a
 
# c
# h
# a
# i
# >>> chai ="He said, \"Masala chai is awesome\""
#   File "<stdin>", line 1
#     chai ="He said, "\Masala chai is awesome"\""
#                       ^
# SyntaxError: unexpected character after line continuation character
# >>> chai ="He said, "\Masala chai is awesome"\"
#   File "<stdin>", line 1
#     chai ="He said, "\Masala chai is awesome"\"
#                       ^
# SyntaxError: unexpected character after line continuation character
# >>> chai ="He said, "\Masala chai is awesome\""
#   File "<stdin>", line 1
#     chai ="He said, "\Masala chai is awesome\""
#                       ^
# SyntaxError: unexpected character after line continuation character
# >>> chai ="He said, \"Masala chai is awesome\""
# >>> chai 
# 'He said, "Masala chai is awesome"'
# >>> chai = "Masala \n Chai"
# >>> print(chai)
# Masala 
#  Chai
# >>> chai =r"Masala\nChai"
# >>> print(chai)
# Masala\nChai
# >>> chai ="Masala Chai"
# >>> chai
# 'Masala Chai'
# >>> print("Masala" in chai )
# True
# >>> print("masala" in chai )
# False
# >>> 