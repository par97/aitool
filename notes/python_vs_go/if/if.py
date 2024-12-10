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