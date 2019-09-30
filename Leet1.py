from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, n in enumerate(nums):
        if n in dic:
            return [dic[n], i]
        dic[target - n] = i


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 13))
