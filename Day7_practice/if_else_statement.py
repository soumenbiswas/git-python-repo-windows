db_group=["user1","user2","user3"]
aap_group=["user4","user5","user6"]
web_group=["user7","user8","user9"]

user_name=raw_input("Enter the name of the user : ")

if user_name in db_group:
    print "user in db group"
elif user_name in aap_group:
    print "user in app group"
elif user_name in web_group:
    print "user in web_group"
else:
    print "the user is not present"
