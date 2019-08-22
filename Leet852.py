from typing import List


class Leet852:

    @staticmethod
    def peak_index_in_mountain_array(a: List[int]) -> int:
        return Leet852.find_peak(a, 0, len(a) - 1)

    @staticmethod
    def find_peak(a: List[int], lo: int, hi: int) -> int:
        if hi >= lo:
            middle = lo + (hi - lo) / 2
            mid = int(middle)
            if a[mid - 1] < a[mid] and a[mid] > a[mid + 1]:
                return int(mid)
            elif a[mid - 1] > a[mid] and a[mid] > a[mid + 1]:
                return Leet852.find_peak(a, lo, mid - 1)
            elif a[mid - 1] < a[mid] and a[mid] < a[mid + 1]:
                return Leet852.find_peak(a, mid + 1, hi)
        return -1

    @staticmethod
    def find_peak_iterative(a: List[int]) -> int:
        lo = 0
        hi = len(a) - 1
        while lo < hi:
            mid = int(lo + (hi - lo) / 2)
            if a[mid] < a[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    mountain = [0, 1, 0]
    mountain2 = [0, 2, 1]
    mountain3 = [0, 1, 2, 3, 4, 1, 0]
    print(Leet852.peak_index_in_mountain_array(mountain))
    print(Leet852.peak_index_in_mountain_array(mountain2))
    print(Leet852.peak_index_in_mountain_array(mountain3))
    print("Iterative solution: ")
    print(Leet852.find_peak_iterative(mountain))
    print(Leet852.find_peak_iterative(mountain2))
    print(Leet852.find_peak_iterative(mountain3))
