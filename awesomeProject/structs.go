package main

type Rectangle struct {
	length, width, height float64
	geometry              struct {
		area      float64
		perimeter float64
	}
}

func (r Rectangle) Area(a, b int) float64 {
	//TODO implement me
	panic("implement me")
}
