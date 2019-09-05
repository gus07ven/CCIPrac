from typing import List

class Leet46:

    def permute(self, nums: List) -> List[List]:
        results = []
        return self.permute_rec(self, results, set(), nums)

    def permute_rec(self, results: List[List], ) -> List[List]:
        return []


if __name__ == "__main__":
    nums = [1, 2, 3]
    result = permute(nums)