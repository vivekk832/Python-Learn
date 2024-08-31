# username = "chaiaurcode"

# def func():
#     username = 'chai'
#     print(username)

# print(username)
# func()



x = 99 
# def func2(y):
#     z = x+y
#     return z

# RES=func2(1)
# print(RES)


# def func3():
#     global x
#     x= 12

# func3()

# print(x)




# def f1():
#     x=88
#     def func2():
#         print(x)
#     return func2
# myResult = f1()
# myResult()



def chaiCoder(num):
    def actual(x):
        return x**num
    return actual 


f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))
print(g(3))


# 9
# 27

