print("hello",'\t',"yes")


string = 'Forritun'
print(string[3:7])

for ch in string:   #character
    print(ch)


string2 = 'skemmtileg'
print(string + " " + string2)

string2 = 'K' +string[::-1]  #frá einum og út restina
print(string2)


string = 'forritun skemmtileg'
print(string.upper())

print(string.split()) #skilar lista  og skiptir í bilinu

#test_str = this is the first item {}, this is the second{}'.format("hello",2)
#print(test_str)



name = input("Input a name: ")
name_str = name
temp = ' '
for st in name_str.split():
    if st == 'gandhi':
        temp += st.title()
   
    if st != 'gandhi':
        temp = st[0].upper() + '.' + temp
        print(temp,end=" ")
 
   
        
