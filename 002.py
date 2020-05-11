# In the name of Allah

number1 = 0   #First number
number2 = 1   #Second number
sum = 0       #Total sum value

while number2 < 4e6:     # 4e6 = 4000000
    number1, number2 = number2, number2 + number1    #Instant changing variables
    """ 
    Another way to changing variables

    temp = number1                
    number1 = number2             =========>>>>>>>>>  If we do not assign number1 to another variable like temp , number1 is gonna equal to new number1 
    number2 = number1 + temp
   
    """
    if number1 % 2 == 0:
        sum += number1

print(sum)    # Answer is 4613732
