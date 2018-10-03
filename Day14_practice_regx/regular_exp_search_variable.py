import re
my_str="Python is a programming language and its easy to learn"

my_matched_ob=re.search("is",my_str)    #this variable is storing the output of re.search()
if my_matched_ob:
    print " 'is' is there in the string"
    print my_matched_ob.group() #this will show the matched word
    print my_matched_ob.start() #this will match the starting index of the matched object
    print my_matched_ob.end() #this will give the value where the string is (ending index +1); end - start will give the length of the string
    print "length of the matched word: ",my_matched_ob.end()-my_matched_ob.start()  #this will print the length of the string

else:
    print "no match found, sorry !"
