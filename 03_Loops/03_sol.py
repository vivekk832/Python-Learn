# Multiplication Table Printer
# print the multiplication table for the given number up to 10 , skip the fifth iteration 
number= 3
for i in range(1,11):
    if i==5:
        continue 
    print(number,'x',i,'=',number*i)