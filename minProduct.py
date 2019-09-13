
def minProduct(a: int, b: int) -> int:
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)


def minProductHelper(smaller: int, bigger: int) -> int:
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    s = smaller >> 1
    halfProduct = minProductHelper(s, bigger)

    if smaller % 2 == 0:
        return halfProduct + halfProduct
    else:
        return halfProduct + halfProduct + bigger


if __name__ == "__main__":
    print(minProduct(3, 5))
