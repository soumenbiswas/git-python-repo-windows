#suppose we need to find some files that are present
#list
my_list_files=[".txt",".log",".sh",".py"]
print my_list_files
#suppose we have these files with us, and .log file is not there, so we can delete the .log files from the list
#list are immutable


#tuple
my_list_files=(".txt",".log",".sh",".py")
print my_list_files
#we cannot remove .log files from the tuple (tuples are immutable)

#---------------------------------------------------------
#real life situation

#suppose configurations files and application server files are there, so its important not to delete by mistake
#those files so, represent those data as a tuple.
'''
my_conf_files=("httpd.conf","conf.xml","server.xml")
'''
