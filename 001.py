#in the name of the Allah

total = 0                # initial total value
 
for number in range(1,1000):  # For all positive numbers to 1000 
    if (number % 3 == 0) or (number % 5 == 0):
        total += number   
    else:
        continue

print(total)            # Answer is 233168