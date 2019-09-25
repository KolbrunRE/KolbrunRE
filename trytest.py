def position(x_coord):
    Highest_val_x = 10
    i = 1
    Val_on_x_ax = ' '

    while i < x_coord:
        Val_on_x_ax += 'x' #Sets 'x' from x = one until the position value

        i += 1

    Val_on_x_ax += 'o'   #Sets 'o' on the posoition value

    while x_coord < Highest_val_x:   
        Val_on_x_ax += 'x'     #Sets 'x' after the position value until value on x-axis is x = 10.

        x_coord += 1

    return Val_on_x_ax

x_coord = int(input("Input a position between 1 and 10:"))
position_choice = position(x_coord)
print(position_choice)

print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

x_coord1 = x_coord


def choice(choice):
    while choice == 'l' or choice == 'r':
    
        if choice == 'l' and x_coord != 1:
            x_coord -= 1   #the position value is now one lower then before

        elif choice == 'r' and x_coord != 10:
            x_coord += 1   #the position value is now one higher then before

        else:
            x_coord = x_coord
        
    return x_coord

choice1 = input("Input your choice:")
position_choice = choice(choice1)
position_choice = position(x_coord)
print(position_choice)







        
