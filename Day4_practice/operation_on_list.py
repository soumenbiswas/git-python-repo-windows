x=[2,434,564,63,21,5545]

#sort operation
#use of sort operation on list
x.sort()
print x
print "---------"

#reverse and sort operations
#use of reverse operation on my_list
x=[2,434,564,63,21,5545]
x.reverse()
print x
print "---------"

#to print the string in decending order
x.sort()
x.reverse()
print x

x.sort(reverse=True)
print x

print "---------"

#append operation
#to append data into a my_list

x=[2,434,564,63,21,5545]
x.append("hello")
print x

#insert operation
#to insert data into a my_list
x=[2,434,564,63,21,5545]
x.insert(3,47)   #provide index value and then the data
print x

#pop operation:
#this will act on index position and pop the data output
x=[2,434,564,63,21,5545]
x.pop(1)
print x

#remove operations
x=[2,434,564,63,21,5545]
x.remove(21)
print x
