def anyfunction():
    print "This is a function without any arguments"
    print "Thsi is without returning value"
def second_function(a,b):
    print "this is with arguments"
    print "a = {} and b = {}".format(a,b)
    print "this is without a retrun value"
def addition(x,y):
    z=x+y
    return z
def substraction(p,q=10):   #setting value in the same function
    r=p-q
    return r



anyfunction()
second_function(4,5)
#passing value to the second function from the main program
a=6
b=7
second_function(a,b)
#we are passing value to the addition() function and also returning the value
sum=addition(10,20)
print "sum of the addition is: ",sum

sub=substraction(50)     #passing one value to the function; it will take another value that is defined in the second_function
print "substraction of the numbers is",sub
