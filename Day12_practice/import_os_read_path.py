#input path and it will seach the specific file/folder in the path:

import os

usr_path=raw_input("Enter your path: ")
usr_req_file=raw_input("Enter your required file: ")

all_f_d=os.listdir(usr_path)

#print "your files and directories in given path are: ", all_f_d

if usr_req_file in usr_path:
    print "The file: {} is in the given path: {}".format(usr_req_file,usr_path)
else:
    print("your file is not there in the given path")
