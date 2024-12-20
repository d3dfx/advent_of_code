package one

import (
	"fmt"
	// "sort"
	"math"
	"slices"
	"strconv"
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
	loc_list1, loc_list2 := split_loc_lists(input)

	slices.Sort(loc_list1)
	slices.Sort(loc_list2)

	total_dist := 0
	for idx := 0; idx < len(loc_list1); idx++ {
		total_dist = total_dist + int(math.Abs((float64(loc_list1[idx] - loc_list2[idx]))))
	}

	return strconv.Itoa(total_dist)
}

func partTwo(input string) string {
	return ""
}

func split_loc_lists(loc_lists string) (loc_list1, loc_list2 []int) {

	for _, loc := range strings.Split(loc_lists, "\n") {
		tmp1, tmp2, found := strings.Cut(loc, "   ")

		left_elem, _ := strconv.Atoi(tmp1)
		right_elem, _ := strconv.Atoi(tmp2)

		if found {
			loc_list1 = append(loc_list1, left_elem)
			loc_list2 = append(loc_list2, right_elem)
		}
	}
	return loc_list1, loc_list2
}
