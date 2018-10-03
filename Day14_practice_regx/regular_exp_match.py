import re

my_str="python is easy to learn language"
my_pat="is"

print "1"

print re.match(my_pat,my_str)   #this will give a output of none, but "is" is there in the string

print "2"
print re.match("python",my_str)
