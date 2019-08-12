
class Leet832:

    def flip_and_invert_image(self, a):
        return [[1 - i for i in row[::-1]] for row in A]

    def flip_and_invert_image_2(self, a):
        for row in A:
            i, j = 0, len(row) - 1
            while i <= j:
                if row[i] == row[j]:
                    row[i], row[j] = row[i] ^ 1, row[j] ^ 1
                i += 1
                j -= 1
        return A


if __name__ == '__main__':
    obj832 = Leet832()
    A = [[1, 1, 0, 0],
         [1, 0, 0, 1],
         [0, 1, 1, 1],
         [1, 0, 1, 0]]
    print(obj832.flip_and_invert_image(A))
