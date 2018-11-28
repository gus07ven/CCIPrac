import sys
import time

number = input("Hello! Please enter a number:  ")
print("The starting number is " + number)

for i in range(int(number), sys.maxsize):
    isPrime = True
    for num in range(2, i):
        if i % num == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
        time.sleep(1)


