#we can take multiple values in a list which can be int,float,string

x=[5,6,7,8,9,10,"hello",7.6]  #list
print type(x)
print x
#index starts from 0; so the first value index is 0
print x[6]

#we can use negative index also
print x[-1]

#to get data in a range
print x[1:3]

#to get data after a specific indexes
print x[3:]

#to get data before a specific indexes

print x[:7]
#------------------------------------------------------------------

#to get list from a list

my_list=[12,"hello",[434,35,75,12,54],435,"hi"]

print my_list[2]    #this will get the inside list; because it will treat it as a entire data
print my_list[2][3] #to get data from a list and the data inside of the list
