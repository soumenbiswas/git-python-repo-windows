group1=["user1","user2","user3"]      #user to start DB servers
group2=["user4","user5"]

user_name=raw_input("Enter your name: ")

if user_name in group1:
    print "this user is in group1"
    print "you are allowed to start DB servers"
if user_name in group2:
    print "this user is in group2"
    print "you are allowed to start APP servers"
