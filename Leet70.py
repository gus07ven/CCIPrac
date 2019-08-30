from typing import List


class Leet70:

    @staticmethod
    def climb_stairs(n: int) -> int:
        steps_table = [0] * (n + 1)
        return Leet70.climb_stairs_aux(steps_table, n)

    @staticmethod
    def climb_stairs_aux(steps_table: List[int], n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        if steps_table[n] == 0:
            steps_table[n] = Leet70.climb_stairs_aux(steps_table, n - 2) + Leet70.climb_stairs_aux(steps_table, n - 1)
        return steps_table[n]


if __name__ == "__main__":
    num_steps = 5
    print("The number of distinct ways to climb to the top of a {0:d} step staircase is: {1:d}"
          .format(num_steps, Leet70.climb_stairs(5)))
