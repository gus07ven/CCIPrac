
class Leet832:

    def flip_and_invert_image(self, a):
        return [[1 - i for i in row[::-1]] for row in A]


if __name__ == '__main__':
    obj832 = Leet832()
    A = [[1, 1, 0, 0],
         [1, 0, 0, 1],
         [0, 1, 1, 1],
         [1, 0, 1, 0]]
    print(obj832.flip_and_invert_image(A))
