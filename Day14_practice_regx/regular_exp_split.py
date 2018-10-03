#how to split a string based on two parameters suppose "is" & "to", with in a same list
#take a variable and split the string and store in it

import re

my_str="python is a easy language to learn"
#split the string where there is "is" and "to"

my_pat="[is][easy]"

print re.split(my_pat,my_str)
