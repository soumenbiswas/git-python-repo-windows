import re
my_str="adfasdf@gmail.com hi adfasdf@asfsa.org fasdfsd afa@xyz.in how asfasdfasfasf@yahoo.com asdf asdf ads adfs@facebook.com"

my_pat=r"@\w+\.\w+"

print re.search(my_pat,my_str).group()
print re.findall(my_pat,my_str)

my_pat_ob=re.compile(r"@\w+\.\w+")

print my_pat_ob

print my_pat_ob.search(my_str).group()
print my_pat_ob.findall(my_str)

