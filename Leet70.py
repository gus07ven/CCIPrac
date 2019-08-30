from typing import List


class Leet70:

    @staticmethod
    def climb_stairs(self, n: int) -> int:
        stepsTable = [0] * (n + 1)
        return climb_stairs_aux(stepsTable, n)

    @staticmethod
    def climb_stairs_aux(self, stepsTable: List[int], n: int) -> int:
        pass


if __name__ == "__main__":
    print(Leet70.climb_stairs(5))
