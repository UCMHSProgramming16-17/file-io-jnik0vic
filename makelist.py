# open a file called "list.txt" in write mode

file = open('list.txt', 'w')

#repeat this 10 times
    # take user input
    # write user input to a file
    
count = 1
while count < 11: 
    userinput = input("Enter an Input " + str(count) + ": ")
    file.write(userinput + '\n')
    count+=1
    
# close your file

file.close()