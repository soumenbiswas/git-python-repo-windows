import re
my_ip_line="my IP is : 255.168.0.34"
my_ip1="my IP is : 255.168.000.34"
my_ip2="my IP for this PC is: 0.200.45.244"

my_pat=r"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
my_ip3="ad ded fsaf gef e 333.222.111.121"

print re.findall(my_pat,my_ip3)
print re.findall(my_pat,my_ip1)         #this will print blank value
print re.findall(my_pat,my_ip2)         #this will print blank value

print "======================================"
#--------------------------------------------------
#best way to do this will be: take the pattern like this :
my_pat1=r"\d+\.\d+\.\d+\.\d+"
print re.findall(my_pat1,my_ip3)
print re.findall(my_pat1,my_ip1)
print re.findall(my_pat1,my_ip2)
c
