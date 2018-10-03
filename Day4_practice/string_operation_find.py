#to find some word or letter in a given string we use find operation
#in if conditions we basically use this putput value of find to take some decision
my_string="this is python class"
print my_string.find("python") #output will be the index value of the word from where it starts
print my_string.find("word")    #if the word is not present it will give -1 as default output

new_var=my_string.find("python")    #taking the output into a variable
print new_var

new_var=my_string.find("t",1)   #searching the required word after 1st index, index starts from 0
print new_var

new_var=my_string.find("t",11) #searching after a specific index; if its not present it will give -1
print new_var

new_var=my_string.find("t",5,11) #serch between certain range of indexes
print new_var
