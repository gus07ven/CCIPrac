from typing import List


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

    def rec_permute_list(self, results: List[str], so_far: str, rest: str) -> List[str]:
        if len(rest) == 0:
            results.append(so_far)
        else:
            for i in range(0, len(rest)):
                a = rest[:i]
                b = rest[i + 1:]
                remaining = a + b
                self.rec_permute_list(results, so_far + rest[i], remaining)
            return results


if __name__ == "__main__":
    permuter = StrPermute()
    permuter.rec_permute("", "abc")
    print()
    print("Results from list: ")
    result = permuter.rec_permute_list([], "", "abc")
    for i in result:
        print(i)
