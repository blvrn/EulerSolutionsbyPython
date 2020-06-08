# In the name of Allah

"""Problems

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""


n = 600851475143

for i in range(2,n):
    if  n % i == 0:
        n /= i 
        if n == 1:
            print(i)

