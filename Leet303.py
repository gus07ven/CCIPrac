from typing import List


class Leet303:

    def __init__(self, nums: List):
        self.numsDic = {}
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                self.numsDic[(i, j)] = sum

    def sum_range(self, i: int, j: int) -> int:
        return self.numsDic[(i, j)]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    le = Leet303(nums)
    print(le.sum_range(0, 2))
    print(le.sum_range(2, 5))
    print(le.sum_range(0, 5))
