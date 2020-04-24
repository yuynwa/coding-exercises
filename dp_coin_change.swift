/*
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0


Example
    Example1

        Input:
        [1, 2, 5]
        11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

    Example2

        Input:
        [2]
        3
        Output: -1

*/

func iconChangeRecursive(_ nums: [Int], _ ammount: Int) -> Int {

    if ammount == 0 {
        return 0
    }

    // -100 fix Int.max + 1 overflow
    var result = Int.max - 100

    for n in nums {

        if ammount >= n {
            let prev = iconChangeRecursive(nums, ammount - n)
            result = min(result, prev + 1)
        }
    }
    return result
}

func iconChangeDynamicProgramming(_ nums: [Int], _ ammount: Int) -> Int {

    var steps = Array(repeating: Int.max - 100, count: ammount + 1)
    steps[0] = 0

    for x in 1...ammount {
        for n in nums {
            if x >= n {
                steps[x] = min(steps[x], steps[x - n] + 1)
            }
        }
    }

    if steps.last == Int.max - 100 {
        steps[ammount] = 0
    }
    return steps[ammount]
}


let steps1 = iconChangeRecursive([2,5,7], 27)
print("iconChangeRecursive: \(steps1)")


let steps2 = iconChangeDynamicProgramming([2,5,7], 27)
print("iconChangeDynamicProgramming: \(steps2)")
