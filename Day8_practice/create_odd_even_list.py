#seperate the even and odd numbers from the lists:
#one:even number lists      second:odd number lists

print "Enter only 7 items in the list with []"c
my_numbers=input("Enter your list : ")

even_list=[]
odd_list=[]


rem_number=my_numbers[0]%2
if rem_number==0:
    even_list.append(my_numbers[0])
else:
    odd_list.append(my_numbers[0])

rem_number=my_numbers[1]%2
if rem_number==0:
    even_list.append(my_numbers[1])
else:
    odd_list.append(my_numbers[1])

rem_number=my_numbers[2]%2
if rem_number==0:
    even_list.append(my_numbers[2])
else:
    odd_list.append(my_numbers[2])

rem_number=my_numbers[3]%2
if rem_number==0:
    even_list.append(my_numbers[3])
else:
    odd_list.append(my_numbers[3])

rem_number=my_numbers[4]%2
if rem_number==0:
    even_list.append(my_numbers[4])
else:
    odd_list.append(my_numbers[4])

rem_number=my_numbers[5]%2
if rem_number==0:
    even_list.append(my_numbers[5])
else:
    odd_list.append(my_numbers[5])

rem_number=my_numbers[6]%2
if rem_number==0:
    even_list.append(my_numbers[6])
else:
    odd_list.append(my_numbers[6])


print "The even number list is: ",even_list
print "The odd number list is: ",odd_list
