from typing import List


class Leet46:

    def permute(self, nums: List) -> List[List]:
        results = []
        self.backtrack(results, [], set(), nums)
        return results

    def backtrack(self, results: List[List], soFar: List, soFarSet: set, nums: List) -> None:
        if len(soFar) == len(nums):
            add = soFar.copy()
            results.append(add)
        else:
            for i in nums:
                if i in soFarSet:
                    continue
                soFarSet.add(i)
                soFar.append(i)
                self.backtrack(results, soFar, soFarSet, nums)
                soFarSet.remove(i)
                soFar.remove(i)


if __name__ == "__main__":
    nums = [1, 2, 3]
    le = Leet46()
    result = le.permute(nums)
    for i in result:
        print(i)