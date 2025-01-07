package two

import (
	"fmt"
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
	reports := cleanArr(strings.Split(input, "\n"))
	var safeTotal int = 0
	for _, report := range reports {
		var levels = strings.Split(report, " ")
		var level_inc bool
		var safe bool = true
		for idx := 0; idx < len(levels)-1; idx++ {

			current, err := strconv.Atoi(levels[idx])
			next, err := strconv.Atoi(levels[idx+1])

			if err != nil {
				fmt.Println(err.Error())
				continue
			}

			diff, inc := absInt(current, next)

			if idx == 0 {
				level_inc = inc
			}

			if diff > 3 || diff == 0 || level_inc != inc {
				safe = false
			} else {
			}
		}

		if safe {
			safeTotal = safeTotal + 1
		}
	}
	return strconv.Itoa(safeTotal)
}

func partTwo(input string) string {
	return input
}

// func split_loc_lists(loc_lists string) (loc_list1, loc_list2 []int) {
// 	return loc_list1, loc_list2
// }

func cleanArr(arr []string) []string {
	var newArr []string
	for idx := 0; idx < len(arr)-1; idx++ {
		if arr[idx] != "" {
			newArr = append(newArr, arr[idx])
		}
	}
	return newArr
}

func absInt(x int, y int) (int, bool) {

	if x < y {
		return y - x, false
	} else {
		return x - y, true
	}
}
