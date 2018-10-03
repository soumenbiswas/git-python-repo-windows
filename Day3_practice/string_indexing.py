#suppose we need to extract specific character from a length_of_string then we use indexing of stringself.

name="soumen"

print name
string_length=len(name)
print string_length

print "================"
#lets we want to extract u from the given stringself
#---------------------------------------------------

print "to extract the letter from a string: ",name[2]

#to print from a specific range of index in stringself
#----------------------------------------------------

range="This is from the Narendra's class"
#we want to extract Narendra's
#use of positive indexes
print range
print "extract with the help of positive indexes: ",range[17:27]

#use of negative indexes

print "extract with the help of negative indexes: ",range[-16:-6]


#printing strings into lower and upper case

low_up="sOUmen biSwAs"

print low_up.lower()
print low_up.upper()

#print string with title()

print low_up.title()

#print sting with capitalize()

print low_up.capitalize()


#to check the string is in title format or not with istittle()

prog="this is narendra's class"
print prog.istitle()

print prog.startswith('t')
