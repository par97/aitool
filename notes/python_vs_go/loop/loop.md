# 循环语法

## Python

for 循环

```python
for w in words:
	print(w, len(w))
```

python 使用 range 函数来生成一个整型序列，这个序列的长度是可以指定的。
```
for i in range(10):
	print(i)
```

for 循环使用 enumerate

```python
for i, element in enumerate(seq):
	print(i, element)
```

python 可以使用 while 循环

```python
while i<n:
	print(i, end=" ")
	i+=1
```

## Go

只有 for 循环这一种循环语句，for 循环的这三个部分每个都可以省略

```go
for initialization; condition; post {

}
```


for 循环也可以使用 range 表达式

```go
for i := range 3 {

}

for i, arg := range os.Args {

}
```


