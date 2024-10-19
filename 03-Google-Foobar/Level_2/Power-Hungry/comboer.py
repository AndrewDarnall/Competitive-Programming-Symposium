class Combinations:

    def __init__(self, arr):
        self.arr = arr
        self.max = arr[0]

    def generate_combinations(self, arr, current_combination=[]):
        if not arr:
            # print(current_combination)
            prod = 1
            for i in range(len(current_combination)):
                prod *= current_combination[i]
            if prod > self.max:
                self.max = prod
            return
        # The left portion to include
        self.generate_combinations(arr[1:], current_combination + [arr[0]])
        # The right portion - the left portion, where the recursion continues
        self.generate_combinations(arr[1:], current_combination)



# combos = Combinations([2, -3, 1, 0, -5])
# combos.generate_combinations(combos.arr)
# print("The Maximum value is:\t{}".format(combos.getMax()))
def solution(xs):
    combos = Combinations(xs)
    combos.generate_combinations(combos.arr)
    return str(combos.max)

print(solution([1, 2, 3, 4, 5]))