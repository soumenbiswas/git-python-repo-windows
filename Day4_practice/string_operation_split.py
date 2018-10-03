my_string="this is python class"
print my_string.split()     #by default where there is a space the division will be done, and it will be in a form of list

#we can divide based on specific word
print my_string.split("python") #this will be seperated as two values seperated with comma ,

print my_string.split("x") #if we dont have x in our given string; the output will be the entire string
