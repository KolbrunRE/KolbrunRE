n = int(input("Enter the length of the sequence: ")) # Do not change this line

first = 1
second = 2
third = 3
i = 0
algorithm = 0

if  n >= 1:
    print(first)
if n >= 2:
    print(second)
if n >= 3:
    print(third)
    for i in range(3,n):  #have already printed out the first three
        algorithm = first + second + third
        print(algorithm)
    
        first = second
        second = third 
        third = algorithm
        i += 1