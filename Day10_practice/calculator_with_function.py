def my_info():
    print "============================"
    print "This is a calculator program"
    print "============================"

def my_menu():
    print "Enter 1 for addition: "
    print "Enter 2 for substraction"
    print "Enter 3 for multiplication"
    print "Enter 4 for division"


def addition(x,y):
    sum=x+y
    print sum
def substraction(x,y):
    sub=x-y
    print sub
def multiplication(x,y):
    mul=x*y
    print mul
def division(x,y):
    div=float(x/y)
    print div


def main():
    my_info()
    x=input("Enter your first number: ")
    y=input("Enter the second number: ")
    print "========================"
    my_menu()
    user_req=input("please input your option for arithematic process: ")

    if user_req == 1:
        addition(x,y)
    elif user_req ==2:
        substraction(x,y)
    elif user_req ==3:
        multiplication(x,y)
    elif user_req ==4:
        division(x,y)
    else:
        print "your option is invalid"
main()
