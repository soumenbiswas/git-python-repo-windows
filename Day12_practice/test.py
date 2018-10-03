import os

path ="C:\\Python27\\Lib\\soumen"
print path
if os.path.exists(path):
    print "your path is valid"
else:
    print "your path is invalid"
path2="D:\\DRIVE 2(DevOps)\\Devops Tutorials\\Python-Narendra\\Practice\\Day12_practice\\test.py"
print os.path.isdir(path2)
print os.path.isfile(path2)

print os.sep
print os.name
print os.environ
print "********************************************************"
print "On this system the user profile path is: ",os.environ['USERPROFILE']
print "Operating system name is : ",os.environ['os']
