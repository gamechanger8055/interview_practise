package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
	"sync"
)

func (r Rectangle) Perimeter() float64 {
	return float64(2 * (r.width + r.length))
}
func PrintShape() {
	var s Shape
	s = Rectangle{length: 10, width: 20, height: 30}
	fmt.Println(s.Perimeter())

}

var (
	counter int32
	wg      sync.WaitGroup
	mutex   sync.Mutex
)

func ResponseSize(url string, nums chan int) {
	// will run till all goroutines are executed
	defer wg.Done()
	fmt.Println("Step1: ", url)
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Step2: ", url)
	defer response.Body.Close()

	fmt.Println("Step3: ", url)
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Step4: ", len(body))
	nums <- len(body)
}

func RaceCondition() {
	wg.Add(3) // Add a count of three, one for each goroutine.

	go increment("Python")
	go increment("Java")
	go increment("Golang")

	wg.Wait() // Wait for the goroutines to finish.
	fmt.Println("Counter:", counter)

}

func increment(name string) {
	defer wg.Done()
	for range name {
		mutex.Lock()
		{
			counter++
			fmt.Println(name)
		}
		mutex.Unlock()
		//atomic.AddInt32(&counter, 3)
		//runtime.Gosched()
	}
}

func fibChannel(n int, c chan<- int) { // receive only channel
	x, y := 0, 1
	for i := 0; i < n; i++ {
		fmt.Println("go go channel", i, len(c))
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func doSomething(ch chan int) {
	x := 42
	ch <- x // send x on the channel
}

func fibCall() {
	ch := make(chan int)
	go doSomething(ch) // launch a goroutine to do something with x
	go fibChannel(10, ch)
	x := <-ch // receive x from the channel
	fmt.Println(x)
	c := make(chan int, 3)
	go fibChannel(10, c)
	for i := range c {
		fmt.Println(i)
	}
	//unbuffered channel
	for i := 0; i < 10; i++ {
		x := <-ch
		fmt.Println(x)
	}
}

func multipleChannels() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			ch1 <- i
		}
		close(ch1)
	}()

	go func() {
		for i := 10; i < 20; i++ {
			ch2 <- i
		}
		close(ch2)
	}()

	for {
		select {
		case x, ok := <-ch1:
			if ok {
				fmt.Println("Received from ch1:", x)
			} else {
				fmt.Println("ch1 closed")
			}
		case x, ok := <-ch2:
			if ok {
				fmt.Println("Received from ch2:", x)
			} else {
				fmt.Println("ch2 closed")
			}
		}
	}

	cp := make(chan string, 1)

	// Start three goroutines that read from the channel
	for i := 0; i < 3; i++ {
		go func() {
			msg := <-cp
			fmt.Println("Received message:", msg)
		}()
	}

	// Broadcast a message to all the goroutines
	cp <- "Hello, World!"
}

func fileCreation() {
	file, err := os.Create("file.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	_, err = os.Stat("test")
	if os.IsNotExist(err) {
		errDir := os.Mkdir("test", 0755)
		if errDir != nil {
			log.Fatal(err)
		}
	}
	oldName := "file.txt"
	newName := "te.txt"
	err = os.Rename(oldName, newName)
	if err != nil {
		log.Fatal(err)
	}
	filename := "er.txt"
	fileBuffer, err := ioutil.ReadFile(filename)
	if err == nil {
		fmt.Println(err)
		os.Exit(1)
	}
	inputData := string(fileBuffer)
	data := bufio.NewScanner(strings.NewReader(inputData))
	data.Split(bufio.ScanRunes)

	for data.Scan() {
		fmt.Print(data.Text())
	}
}
