package main

import (
	"aoc/2024/one"
	"flag"
	"fmt"
	"log"
	"os"
)

func main() {

	// Day Flag
	var day string
	flag.StringVar(&day, "day", "1", "The AOC day to run")
	flag.StringVar(&day, "d", "1", "The AOC day to run (shorthand)")

	// Part Flag
	var puzzle string
	flag.StringVar(&puzzle, "puzzle", "1", "The AOC puzzle to run")
	flag.StringVar(&puzzle, "p", "1", "The AOC puzzle to run (shorthand)")

	flag.Parse()

	switch day {
	case "1":
		one.RunPart(puzzle, readPuzzleInput("./one/"))
	default:
		fmt.Printf("\nNo day with number %s found\n", day)
	}
}

func readPuzzleInput(folder string) string {

	data, err := os.ReadFile(folder + "input.txt")

	if err != nil {
		log.Fatal(err)
	}

	return string(data)
}
