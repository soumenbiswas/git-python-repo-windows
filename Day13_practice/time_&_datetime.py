#date and datetime module:

#WHEN EVER WE WANT TO PUT SOME DELAY BETWEEN THE EXECUTION OF COMMANDS; BEST OPERATION IS datetime

import time
import datetime

print "hello"
time.sleep(2)
print "bye"
print "------------"

#we can use datetime module to print date

print datetime.date.today().year
print datetime.date.today().month
print datetime.date.today().day
print datetime.datetime.today().hour
print datetime.datetime.today().minute
print datetime.datetime.today().second

#take the datetime value in a variable:

date_today=datetime.datetime.now().strftime("%Y-%m-%d")
print "date is stored in variable: ",date_today
