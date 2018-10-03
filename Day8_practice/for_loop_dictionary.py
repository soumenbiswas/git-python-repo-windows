'''
#dictionary for loop 1st type:
my_dict={"three":3, "four":4, "five":5}


print "The list of keys in the dictionary"
for each in my_dict.keys():
    print each


print "====================================="
print "The list of values in the dictionary"
for each in my_dict.values():
    print each
'''

#dictionary for loop 2nd type:
my_dict={"three":3, "four":4, "five":5}
#print my_dict.items()
for k,v in my_dict.items():         #lets take the keys as k and values as v
    print k                         #to print only the keys
