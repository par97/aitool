
words="hello world"

print("loop1: ", end="")
for w in words:
	print(w, end=' ')
print()

# for 循环使用 enumerate
print("loop2: ", end="")
for i, element in enumerate(words):
	print("%d:%s" % (i, element), end=' ')
print()

# python 可以使用 while 循环
print("loop3: ", end="")
n=10
i=0
while i<n:
	print(i, end=" ")
	i+=1
print()

# python 使用 range 函数来生成一个整型序列，这个序列的长度是可以指定的。
print("loop4: ", end="")
for i in range(10):
	print(i, end=" ")
print()
