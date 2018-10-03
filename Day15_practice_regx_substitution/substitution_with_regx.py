#where ever there is .com is there replace it with .org
import re
my_str="soumen@gmail.com ritu@facebook.com jitu@yahoo.in mitu@outlook.com"

my_pat=r"\.\w+"
print re.findall(my_pat,my_str)

my_pat1=r"\.[ci][on]."      #group first letters together; second letters together; and third letters together and so on
print re.findall(my_pat1,my_str)

my_str1= "nasa@gmail.gov cnn@gmail.us"
my_pat1=r"\.[gu][os]."
print re.findall(my_pat1,my_str1)

print "-----------------------------------"
#substitute with the help of pattern

print re.sub(my_pat,".org",my_str)
