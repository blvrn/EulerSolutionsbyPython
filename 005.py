#In the name of Allah

"""Problems

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def check(n):
    for i in range(1,21):
        if n % i == 0:
            continue
        else:
            return False
    return True

x = 2520

while not check(x):
    x += 2520

print(x)