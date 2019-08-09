
class Ex1p1p16:

    def exR1(self, n: int) -> str:
        if n <= 0:
            return ""
        return self.exR1(n - 3) + str(n) + self.exR1(n - 2) + str(n)


if __name__ == "__main__":
    driver = Ex1p1p16()
    print(driver.exR1(6))