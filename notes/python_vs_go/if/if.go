package main

// if 布尔表达式 {
//    /* 在布尔表达式为 true 时执行 */
// } else {
//   /* 在布尔表达式为 false 时执行 */
// }

// go 没有 elif 这种语法
// if 语句中嵌套 else if...else 语句

func main() {
	for i := 0; i < 10; i++ {
		if i < 5 {
			println(i, "is less than 5")
		} else if i == 5 {
			println(i, "is equal to 5")
		} else {
			println(i, "is greater than 5")
		}
	}

	for i := 0; i < 10; i++ {
		if i > 3 && i < 5 {
			println(i, "is between 3 and 5")
		}
	}
}
