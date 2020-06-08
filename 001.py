#in the name of the Allah

""" Problems
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
total = 0                # initial total value
 
for number in range(1,1000):  # For all positive numbers to 1000 
    if (number % 3 == 0) or (number % 5 == 0):
        total += number   
    else:
        continue

print(total)            # Answer is 233168
