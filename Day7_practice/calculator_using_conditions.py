x=input("Enter the first value : ")
y=input("Enter the second value : ")

print "Enter 1  ---> addition"
print "Enter 2  ---> substraction"
print "Enter 3  ---> multiplication"
print "Enter 4  ---> division"

usr_req=input("I am waiting for your option : ")

if usr_req==1:
    print "addition of two numbers is: ", x+y
elif usr_req==2:
    print "substraction of two numbers is: ", x-y
elif usr_req==3:
    print "multiplicaton of two numbers is: ", x*y
elif usr_req==4:
    print "division of two numbers is: ", x/y
else:
    print "user input in invalid"
