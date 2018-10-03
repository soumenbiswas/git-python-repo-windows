'''
#program to display the current path

import os
print os.getcwd()   #it will give the current path where u are

os.chdir("PS D:\DRIVE 2(DevOps)\Devops Tutorials\Python-Narendra\Practice\Day12_practice")
print os.getcwd()

'''
'''
import os
os.mkdir("Narendra")
'''


#to check the path provided exists or not
import os
path="C:\\Python27\\Lib"

print os.path.exists(path)       #not getting the output:invalid systax


#to check the provided path is correct or not:
path ="C:\\Python27\\Lib\\soumen"
print path
if os.path.exists(path):
    print "your path is valid"
else:
    print "your path is invalid"
#to check path provided is directory or file
path2="D:\\DRIVE 2(DevOps)\\Devops Tutorials\\Python-Narendra\\Practice\\Day12_practice\\test.py"
print os.path.isdir(path2)
print os.path.isfile(path2)
#path seperator of the operating system
print os.sep
#name of  OS
print os.name
#print os.environ
print "********************************************************"
print "On this system the user profile path is: ",os.environ['USERPROFILE']
print "Operating system name is : ",os.environ['os']
