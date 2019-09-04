from typing import List

class Leet303_2:

    def __init__(self, nums: List):
        self.sums = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]

    def sum_range(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    le = Leet303_2(nums)
    print(le.sum_range(0, 2))
    print(le.sum_range(2, 5))
    print(le.sum_range(0, 5))