'''
x=[32,423,543,32,123,532,32]

total_count=x.count(32)
print "The total count is: ", total_count

index_num=x.index(32)
print"The fist index of that number is: ",index_num

list_length=len(x)
print list_length
'''
'''
x=[423,543,32,123,32,532,32]
total_count=x.count(32)
print x.count(32)
#print x.index(32)

y=0
for y in range(total_count):
    index_num=x.index(32)
    print index_num
'''



my_list=[5,6,7]
print my_list
#if we want to add single value '13' after a specific index_num; suppose between 5 and 6 we want to add
my_list.insert(1,13)    #1 is the index number and 13 is the value
print my_list
'''
#to insert multiple values
new_list=[9,10,11,12]
new_list.insert(1:2)=(25,54)         #1 is the index position and [25,54] is the list; it will basically replace the index 1
print new_list



list_one=[45,46,47]
list_two=[4,5,6]

list_one.insert(2,list_two)
print list_one
'''
