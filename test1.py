def a_list(value):
    my_list = []
    while value != 'exit1P':
        my_list += value
        value = input("Enter value to be added to list:")
    
    if value == 'exit1':
        print(my_list*3)# Your functions should appear here

value = input("Enter value to be added to list:")# Main program starts here
the_list = a_list(value)
