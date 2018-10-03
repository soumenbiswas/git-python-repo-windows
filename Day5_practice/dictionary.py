#about dictionary
#in dictionary there are two things .1 Keys     2.Values

my_dict={}  #empty dictionary

my_new_dict={1:'one',2:'two',3:'three'}     # 1 is key and one is value for that key
#to print the complete dictionary with keys and values
print my_new_dict
#to print only the Values of key 1
print my_new_dict[1]

#if we have two values for a key then we have to write those values as list or tuples for that specific key
my_dict1={1:['one','ek',],2:['two','do'],3:['three','tin']}


#---------------------------------------------
#WE CAN UPDATE THE NAME VALUE FOR ANY Keys
my_dict2={'name':'soumen','class':'python', 'ansible':'yamel'}
print my_dict2
#changing value for NAME
#if the key is not there it will be added to the dictionary
#if the key is there it will change the crosponding value of the key
#therefor dictionaries are immutable
my_dict2['name']='NARENDRA'
print my_dict2

print"--------------------------------"
#-------------------------------------------------------

#to print only the keys of a dictionary
print my_dict2.keys()

#to print only the values of a dictionary
print my_dict2.values()


#to print the items of the my_list
#this will show the entire items of the lists including the keys and Values
print my_dict2.items()

#------------------------------------------------------------

#set operations on dictionary, union & intersection

my_set1={1,2,3,5,4,4,4}
my_set2={1,3,4,5,}

print my_set1.union(my_set2)
print my_set1.intersection(my_set2)
