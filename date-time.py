import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())

#if we want to display the time with timezone, we have to create a object.
import pytz
ist = pytz.timezone('Asia/kolkata')
print(datetime.datetime.now(ist))

print(datetime.datetime.now().year)

#If you want to display just the year-month-daye, you need to format the result as a string

print(datetime.datetime.now().strftime("%Y-%m-%d"))
#To findout all the parameters we can give to strftime(strftime.org)

print(datetime.datetime.now().strftime("%c"))
#fromtimestamp
print(datetime.datetime.fromtimestamp(1555555))

#If I want to use the submodule datetime directly
from datetime import datetime
print(datetime.now())
print(datetime.max)
print(datetime.min)