# if 语法

## Python

If 语句：
```python
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
else:
    print('More than 0')
```

python中可以用连续的比较，比如：
```python
if 0<x<5:
    print('x is between 0 and 5')
```

## Go
```go
if 布尔表达式 {
   /* 在布尔表达式为 true 时执行 */
} else {
  /* 在布尔表达式为 false 时执行 */
}
```

go 没有 elif 这种语法

if 语句中嵌套 else if...else 语句