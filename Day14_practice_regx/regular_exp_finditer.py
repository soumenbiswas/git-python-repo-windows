#to know about the objects and its strating locations we use finditer operation
#it will give a number which will store all the details of the objects,starting and ending details.
#this is callable-iterator object.
import re
my_str="Python is a programming language and its easy to learn"
my_pat="[it][so]"
print re.finditer(my_pat,my_str)

#to print for each objects:
#when it is printing exclusively ; its not showing callable
for each_obj in re.finditer(my_pat,my_str):
    print each_obj, each_obj.group(), each_obj.start(), each_obj.end()
