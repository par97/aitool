# If 语句：
for x in range(10):
    if x < 5:
        print(x, 'is less than 5')
    elif x == 5:
        print(x, 'is equal to 5')
    else:
        print(x, 'is greater than 5')

# python中可以用连续的比较，比如：
for x in range(10):
    if 3<x<5:
        print(x, 'is between 3 and 5')

# python 中还可以使用 if else 语句进行赋值，等同于三元运算符
for x in range(10):
    y= x+10 if x<5 else x+100
    print(y, end=' ')