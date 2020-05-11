# In the name of Allah


n = 600851475143

for i in range(2,n):
    if  n % i == 0:
        n /= i 
        if n == 1:
            print(i)

