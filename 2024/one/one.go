package one

import (
	"fmt"
	"strings"
)

func RunPart(part string, puzzleInput string) {
	if part == "1" {
		fmt.Println(partOne(puzzleInput))
	} else if part == "2" {
		fmt.Println(partTwo(puzzleInput))
	} else {
		fmt.Printf("The reported part %s does not exist", part)
	}
}

func partOne(input string) string {
	a, b := split_loc_lists(input)
	fmt.Println(a)
	fmt.Println(b)
	return ""
}

func partTwo(input string) string {
	return ""
}

func split_loc_lists(loc_lists string) (loc_list1, loc_list2 []string) {
	for _, loc := range strings.Split(loc_lists, "\n") {
		var loc_list1 []string
		var loc_list2 []string
		tmp1, tmp2, found := strings.Cut(loc, "   ")
		if found {
			loc_list1 = append(loc_list1, tmp1)
			loc_list2 = append(loc_list2, tmp2)
		}
	}
	return loc_list1, loc_list2
}
