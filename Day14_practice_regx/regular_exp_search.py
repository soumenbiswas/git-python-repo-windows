#how to search a specific item in a string

import re
my_str="python is easy to learn language"
#search "is" is there or not in the string
my_pat="is"
print "1"
print re.search(my_pat,my_str)

#if we are getting somthing in tht output then the word is there in the given string

print "2"
print re.search("soumen",my_str)    #word is not present in the string

#if the required search is not there, it will print none

#if we want to ignore the case-sensitivity then we have to write:# re.I:
print "3"
print re.search("python",my_str,re.I)
print "4"
print re.search(my_pat,my_str)
