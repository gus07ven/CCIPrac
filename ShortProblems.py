# Add the weighted mean of two arrays without using numpy
# Parameters
# n (int) = number of elements
# x (list of ints) = scores
# w (list of ints) = weights of scores

# Sample inputs
# 5
# 10 40 30 50 20
# 1 2 3 4 5

# Sample output
# 32.0

n = input("Please enter the number of elements to calculate the weighted mean: ")
x = list(map(int, input("Enter a sequence of numbers separated by a space: ").split()))
w = list(map(int, input("Enter a sequence of weights separated by a space (must be the same length of previous sequence: ").split()))

weighted_mean = sum([i * j for i, j in zip(x, w)]) / sum(w)
print("The weighted mean is: ", weighted_mean)