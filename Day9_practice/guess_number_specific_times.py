print "************************************"
print "!!Let's play guess number game !!"
print "************************************"
guess_no=67


# guess the number for specifc chances given to the user_number
print " You will get only 3 chances"

for each in range(3):
    user_number=input("Enter your guess number: ")

    if user_number == guess_no:
        print "your guess is correct"
    else:
        print "***********************"
        print "your guess is wrong"
        print "***********************"

print "ALL YOUR CHANCES ARE OVER"
print "*** !! GAME OVER !! ***"
print "*************************"
