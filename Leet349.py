from typing import List


class Leet349:

    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    for i in Leet349.intersection(nums1, nums2):
        print(i)


