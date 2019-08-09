class Ex1p1p18:

    def mystery(self, a: int, b: int) -> int:
        if b == 0:
            return 0
        if b % 2 == 0:
            return self.mystery(a + a, b // 2)
        return self.mystery(a + a, b // 2) + a


if __name__ == "__main__":
    driverObj = Ex1p1p18()
    print(driverObj.mystery(2, 25))
