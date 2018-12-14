from timeit import Timer


def sum(n):
    if n <= 0:
        return 0
    return n + sum(n - 1)


def pair_sum_sequence(n):
    sum = 0
    for i in range(n):
        sum += pairSum(i, i + 1)
    return sum


def pair_sum(a, b):
    return a + b


if __name__ == "__main__":

    t1 = Timer("sum(5)", "from __main__ import sum")
    print("n = 5 took ", t1.timeit(number=5), "milliseconds")

    t2 = Timer("sum(5)", "from __main__ import sum")
    print("n = 50 took ", t2.timeit(number=50), "milliseconds")

    t3 = Timer("sum(5)", "from __main__ import sum")
    print("n = 500 took ", t1.timeit(number=500), "milliseconds")

    t4 = Timer("sum(5)", "from __main__ import sum")
    print("n = 5000 took ", t1.timeit(number=50000), "milliseconds")

    t5 = Timer("pairSumSequence()", "from __main__ import sum")
    print("n = 5 took ", t1.timeit(number=5), "milliseconds")
