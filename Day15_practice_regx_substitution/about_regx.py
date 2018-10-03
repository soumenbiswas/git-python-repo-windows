#get the details of domains with the help of regx
import re
my_str="soumen@gmail.com ritu@facebook.com jitu@yahoo.com mitu@outlook.com"

my_pat=r"@\w+\.\w+"
print re.findall(my_pat,my_str)

# this section of lines will also give the same output; but the execution speed is less
#because before checking the pattern; you are converting everyting into a object;
#and with that object you are searching something into your given string.
my_pat1=re.compile(r"@\w+\.\w+")
print my_pat1.findall(my_str)
