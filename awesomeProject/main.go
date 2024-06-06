package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"sort"
	"strconv"
	"time"
)

var St = "Japan"

type First func(int) int
type Second func(int) First

func SquareSum(x int) Second {
	return func(y int) First {
		return func(z int) int {
			return z*z + x*x + y*y
		}
	}
}

const (
	a = 10
	b = "hey"
	c = 2.2
)

func Concurrency() {
	wg.Add(3)
	fmt.Println("Start Goroutines")
	go PrintShape()
	nums := make(chan int)
	go ResponseSize("https://www.golangprograms.com", nums)
	fmt.Println("heyy", <-nums)
	go ResponseSize("https://coderwall.com", nums)
	fmt.Println("heyy", <-nums)
	go ResponseSize("https://stackoverflow.com", nums)
	fmt.Println("heyy", <-nums)
	wg.Wait()
	time.Sleep(2 * time.Second)
	close(nums)
	fmt.Println("Terminating program")
}
func add(a, b int) int {
	return a + b
}
func calcArea() float64 {
	r := new(Rectangle)
	r.length = 12
	r.width = 45
	r.displayInfo()
	r.geometry.area = r.length * r.width
	return r.geometry.area
}

func (r Rectangle) displayInfo() {
	fmt.Println(r.length, r.width)
}
func readFile() {
	configData, err := ioutil.ReadFile("config.json")
	if err != nil {
		panic(fmt.Sprintf("error found %v", err))
	}
	x := []int{1: 10, 3: 40}
	x = append(x, 900, 800, 91)
	sort.Slice(x, func(i, j int) bool { return x[i] > x[j] })
	//sort.Ints(x)
	//p := reflect.Interface
	//if p.kind != reflect.Array {
	//	panic(fmt.Sprintf("error found %v", err))
	//}
	y := &x
	fmt.Println(string(configData), x, *y)
}

func typeConversion() {
	p, t := "1000", "34.567"
	iv := "hey"
	_, err2 := fmt.Sscan(t, &iv)
	if err2 != nil {
		panic(fmt.Sprintf("look error found %v", err2))
	}
	for k := 1; k < 5; k++ {
		fmt.Println(k)
	}
	strDict := map[string]string{"Japan": "Tokyo", "China": "Beijing", "Canada": "Ottawa"}
	for key, value := range strDict {
		fmt.Println(key, strDict[key], value)
	}
	for i, u := range "hello" {
		fmt.Println("hello", i, u) //unicode and index
	}
	//infinite loop
	for {
		fmt.Println("hello world")
		break
	}
	r, er := strconv.ParseFloat(t, 64)
	q, err := strconv.Atoi(p)
	fmt.Println(q, reflect.TypeOf(q), err, r, er, iv)
}
func usingPointers(a *float64, b *string) (*float64, *string) {
	*a = *a + 5
	*b += "world"
	return a, b
}

func variadic(a ...interface{}) []interface{} {
	return a

}

func decrementMain() {
	//var slices = make([]int, 10, 20)
	//defer func() {
	//	if r := recover(); r != nil {
	//		fmt.Printf("An error occurred: %v\n", r)
	//		fmt.Println("Application terminated gracefully.")
	//	} else {
	//		fmt.Println("Application executed successfully.")
	//	}
	//}()
	fmt.Println(calcArea())

	//readFile()
	fmt.Println(variadic(1, "red", true, 10.5, []string{"foo", "bar", "baz"},
		map[string]int{"apple": 23, "tomato": 13}))
	fmt.Println(SquareSum(5)(7)(8))
	//Abc()
	typeConversion()
	fmt.Println(add(3, 4))
	i, j := 10.0, 20.0
	t := "hello"
	p, q := usingPointers(&i, &t)
	fmt.Println("rferf", *p, *q)

	if x := 10; x == 20 {
		fmt.Println(x)
	}
	switch i {
	case a, j:
		fmt.Println(i)
		fallthrough
	case c:
		fmt.Println("hey", i)
		fallthrough
	default:
		fmt.Sprintf("hello")
	}
	var Happy int
	fmt.Println(float32(i/j), St, Happy, a, b, c, reflect.TypeOf(i))
}

func main() {
	decrementMain()
	//Concurrency()
	RaceCondition()
	fibCall()
	//multipleChannels()
	fileCreation()
}
