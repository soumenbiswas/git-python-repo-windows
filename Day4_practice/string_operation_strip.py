'''
#strings are immutable, we cannot change a part of a string, but we can change
#the entire string

my_string= "This is a python class"
print my_string

my_string= "now the string is changed"
print my_string
'''

'''
#strip operation 'to strip the spaces from a string'
x1=" hello hw r u? "  #space on both the sides
print x1
x2=" i am fine" #space on left sides
print x2
x3="thank you! "    #space on the right sides
print x3

print "=============="
print "to strip spaces from both the sides"
print x1.strip()
print "=============="
print "to strip space from the left side"
print x2.lstrip()
print "=============="
print "to strip space from the right side"
print x3.rstrip()

'''
#Deleting specific words or letters
my_string="java 1.7.0_216" #want to strip java from the strings
print my_string
print my_string.strip("java ")
#we can store the stip into a variable
my_java=my_string.strip("java ")
print "my_java variable"
print my_java
#using multiple strip
new_str="hello is that me you looking for?"
print new_str.strip("hello").strip()
