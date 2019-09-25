import math
                
for ten_digit in range(10,91,10): #the ten in a two digit number
    for units_digit in range(1,10): #the units in a two digit number 
        if math.sqrt(ten_digit + units_digit) == ((ten_digit/10) + units_digit):
            print(ten_digit + units_digit)



num = 10 #b
divisor_num = 0
while num < 100: # only two digit numbers
    if num % 2 == 0:
        for num2 in range(1,num+1):
            if num % num2 == 0:
                divisor_num += 1
                if num2 == num and divisor_num == 10:
                    print(num,end=" ")
    divisor_num = 0
    num += 1



    
