import re
my_str="adfasdf@gmail.com hi adfasdf@asfsa.org fasdfsd afa@xyz.in how asfasdfasfasf@yahoo.com asdf asdf ads adfs@facebook.com"
#.com and .in 
my_pat=r"\.\w+"
my_pat=r"\.[ci][on]."

print re.findall(my_pat,my_str)

'''
my_str="afdsasdf@pqr.gov asdfasf@dfgafd.us asdfsa asdfds @fasfd.com"
#.gov .us 
my_pat=r"\.[gu][os]."
my_pat=r"\.\w+"
print re.findall(my_pat,my_str)
'''
print re.sub(my_pat,".org",my_str)