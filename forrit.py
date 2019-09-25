#hallo

max_int = 0
num_int = 0

while 0 <= num_int:
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int)    # Do not change this line

