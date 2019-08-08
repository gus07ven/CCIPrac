
class Leet709:

    def to_lower_case(self, s):
        return s.lower()

    def to_lower_case_imp(self, s):
        if len(s) == 0:
            return ""

        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s)


if __name__ == "__main__":
    runner = Leet709()
    input = "HELLO"
    print(runner.to_lower_case(input))
    print(runner.to_lower_case_imp(input))