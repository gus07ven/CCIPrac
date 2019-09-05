class StrPermute:

    def rec_permute(self, so_far: str, rest: str) -> None:
        if len(rest) == 0:
            print(so_far)
        else:
            for i in range(0, len(rest)):
                a = rest[:i]
                b = rest[i + 1:]
                remaining = a + b
                self.rec_permute(so_far + rest[i], remaining)


if __name__ == "__main__":
    permuter = StrPermute()
    permuter.rec_permute("", "abc")
