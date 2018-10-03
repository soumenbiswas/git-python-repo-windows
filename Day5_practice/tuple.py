
#about tuple:
my_tuple=(3,4,5)

print my_tuple
print type(my_tuple)
print len(my_tuple)

#----------------------------------
#blank tuple
empty_tuple=()
print empty_tuple
print type(empty_tuple)

#-----------------------------------
#type of tuple
x=5,6,7         #this is a tuple
print x
print type(x)    #the type it will show as a tuples

#------------------------------
#fetching output from tuple
p=(5,6,43,54,6656,8,335,534)

print p[-1]
print p[1]

print p     #this will give entire tuple
print p[:]  #this will give the entire tuple
print p[1:4]    #this will give the range of the tuple


#-----------------------------------
#jumping indexes
j=(33,51,54,51,54,546,76543,2345,889)
print j[1:6:2]      #the range it will print 1-6 ; and it will jump indexes 1+2=3, after printing the 1st index.


#------------------------------------
#tuple_inside_tuple

tuple_inside=(21,334,543,(432,643,122,54),4534,654,23)
print type(tuple_inside)
print tuple_inside[3][2]    #print 122 from the tuple inside tuple
