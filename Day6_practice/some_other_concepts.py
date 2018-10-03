my_str="python"
my_list=[2,3,4,5,6,7,8,9]
my_tuple=(3,3,4,6,7,8)
my_dict={3:'three',4:'four'}
#--------------------------
# len() function

print "=================================================="
print my_str
print "length of string is: ",len(my_str)
print my_list
print "length of list is: ",len(my_list)
print my_tuple
print "length of my tuple is: ",len(my_tuple)

#in the case of dictionary len() will give only the number of keys used in it.
print my_dict
print "length of my dictionary is :",len(my_dict)

my_list1=[2,3,4,[32,45,64],5,6,7,8,9]
print my_list1
print "length of list inside list is: ",len(my_list1)     # inside list will be calculate as a singl item

print "==================================="
#--------------------------------------------------------------

#max function()
# max() function for string will calculate the numbers max with ASCI values.
print"maximum value in string", max(my_str)         #output : 'y' because the ASCI value of y is 121 which is the highest here
# we can find the max value present in the list or tuple
print "maximum value in list",max(my_list)
print "maximum value in tuple",max(my_tuple)
#--------------------------------------------------------------------
#list inside a list.
