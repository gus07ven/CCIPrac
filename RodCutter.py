from typing import List, Dict


class RodCutter:

    def __init__(self, price_table, rod_length):
        self.price_table = price_table
        self.rod_length = rod_length

    def top_down_dyn_prog_imp(self, price_table: List[int], rod_size: int) -> int:
        if rod_size == 0:
            return 0

        maxRevenue = 0
        for i in range(1, rod_size):
            maxRevenue = max(maxRevenue, price_table[i] + self.top_down_dyn_prog_imp(price_table, rod_size - i))
        return maxRevenue

    def top_down_memo(self, price_table: List[int], rod_size: int) -> int:
        revenue_table = [-1] * (rod_size + 1)
        return self.top_down_memo_aux(price_table, rod_size, revenue_table)

    def top_down_memo_aux(self, price_table: List[int], rod_size: int, revenue_table: List[int]) -> int:
        if revenue_table[rod_size] >= 0:
            return revenue_table[rod_size]
        max_revenue = 0
        for i in range(1, rod_size):
            max_revenue = max(max_revenue, price_table[i] +
                              self.top_down_memo_aux(price_table, rod_size - i, revenue_table))
        revenue_table[rod_size] = max_revenue
        return max_revenue


if __name__ == "__main__":
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rod_length = 7
    rc = RodCutter(prices, rod_length)
    print(rc.top_down_dyn_prog_imp(rc.price_table, rc.rod_length))
    print(rc.top_down_memo(rc.price_table, rc.rod_length))
