print "************************************"
print "!!Let's play guess number game !!"
print "************************************"
guess_no=67

#guess infinite number of times untill the perfect  guess.
while True:
    user_number=input("Enter your guess number: ")

    if user_number==guess_no:
        print "your guess is correct"
        break
    else:
        print "your guess is wrong"
