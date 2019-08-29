from typing import List, Dict


class RodCut:

    def __init__(self, price_table, rod_length):
        self.price_table = price_table
        self.rod_length = rod_length

    def top_down_dyn_prog_imp(self, price_table: List[int], rod_length: int) -> int:
        if rod_length == 0:
            return 0

        maxRevenue = 0
        for i in range(1, rod_length):
            maxRevenue = max(maxRevenue, price_table[i] + self.top_down_dyn_prog_imp(price_table, rod_length - i))
        return maxRevenue


if __name__ == "__main__":
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rod_length = 7
    rc = RodCut(prices, rod_length)
    print(rc.top_down_dyn_prog_imp(rc.price_table, rc.rod_length))
