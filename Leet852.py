from typing import List


class Leet852:

    @staticmethod
    def peak_index_in_mountain_array(a: List[int]) -> int:
        return Leet852.find_peak(a, 0, len(a) - 1)


if __name__ == "__main__":
    mountain = [0, 1, 0]
    mountain2 = [0, 2, 1]
    mountain3 = [0, 1, 2, 3, 4, 1, 0]
    print(Leet852.peak_index_in_mountain_array(mountain))
    print(Leet852.peak_index_in_mountain_array(mountain2))
    print(Leet852.peak_index_in_mountain_array(mountain3))
