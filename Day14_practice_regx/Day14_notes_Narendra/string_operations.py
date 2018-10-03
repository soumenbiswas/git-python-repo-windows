import re 
my_str="Python is a programming language and its easy to learn"

#my_matched_ob=re.search("its",my_str)
my_matched_ob=re.match("Python",my_str)

if my_matched_ob:
	print " 'is' is there in given str"
	print my_matched_ob.group()
	print my_matched_ob.start()
	print my_matched_ob.end()
	print "length of matched word: ",my_matched_ob.end()-my_matched_ob.start()
else:
	print "no match "

