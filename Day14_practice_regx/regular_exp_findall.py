#when we need to find multiple match then we use find all operation:
#findall will give the match words but it will not give the info about the starting or ending
#index of any of the words.
import re
my_str="Python is a programming language and its easy to learn"
my_pat="[it][so]"
print re.findall(my_pat,my_str)
