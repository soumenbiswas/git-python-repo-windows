#for repetation of a part of a program we use the loops concept

#print "Enter only 7 items in the list with []"
my_numbers=input("Enter your list : ")

even_list=[]
odd_list=[]

for each_number in my_numbers:
    rem=each_number%2
    if rem==0:
        even_list.append(each_number)
    else:
        odd_list.append(each_number)

print "Even number in the list are ",even_list
print "Odd number in the list are ",odd_list
