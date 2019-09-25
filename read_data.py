# Get filename from user
# Open file
# Read file
# Output data
def open_file(filename):
    file_object = open(filename,"r") # r = read lesa möppuna
    return file_object

def read_file_and_output(file_object,out_object):
    for line in file_object:
        line = line.strip()
        print(line)
        print(line,file=out_object)

def get_line_number():
    line_num = int(input("Enter a line number: "))
    return line_num

def main():
    #filename = input("Enter filename: ")
    line_num = get_line_number()
    print(line_num)
    #file_object = open_file(filename)
    #out_object = open("out.txt","w") # w = write ham - skrifa út í möppuna
    #read_file_and_output(file_object, out_object)
    #file_object.close()
main()