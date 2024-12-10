package main

import "fmt"

// 只有 for 循环这一种循环语句，for 循环的这三个部分每个都可以省略
func loop1() {
	fmt.Print("loop1: ")
	for i := 0; i < 10; i++ {
		fmt.Print(i, " ")
	}
	fmt.Println()
}

func loop2() {
	fmt.Print("loop2: ")
	i := 0
	for ; i < 10; i++ {
		fmt.Print(i, " ")
	}
	fmt.Println()
}

func loop3() {
	fmt.Print("loop3: ")
	i := 0
	for ; ; i++ {
		if i == 10 {
			break
		}
		fmt.Print(i, " ")
	}
	fmt.Println()
}

func loop4() {
	fmt.Print("loop4: ")
	i := 0
	for {
		if i == 10 {
			break
		}
		fmt.Print(i, " ")
		i++
	}
	fmt.Println()
}

// for 循环也可以使用 range 表达式

func loop5() {
	fmt.Print("loop5: ")
	for i := range 10 {
		fmt.Print(i, " ")
	}
	fmt.Println()
}

func loop6() {
	fmt.Print("loop6: ")
	arr := []int{10, 11, 12, 13, 14, 15}
	for i, n := range arr {
		fmt.Printf("%d:%d ", i, n)
	}
	fmt.Println()
}

func main() {
	loop1()
	loop2()
	loop3()
	loop4()
	loop5()
	loop6()
}
