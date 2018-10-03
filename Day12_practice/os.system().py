#we can execute windows commands with the use of os.system()
import os
os.system('dir')
my_output=os.system('dir')      #we cannot take the value of os.system() into a variable
print "**********"
print my_output
print "we cannot catch the value of os.system(), so it will returun value 0"
