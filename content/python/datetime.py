import datetime
import calendar

# Date
today = datetime.date.today() # today's date
today.day # day
today.month # month
today.year # year
today.weekday() # weekday, monday = 0, sunday = 6
today.isoweekday() # human readable weekday, monday = 1, sunday = 7
today.isoformat() # iso format eg. 2024-02-24

# Datetime (combine date and time)
today = datetime.datetime.now() # current date and time
today.hour # hour
today.minute # minute
today.second # second
today.microsecond # microsecond, these are all attributes of datetime
today.timestamp() # timestamp, seconds since 1970
today.date() # same as datetime.date
today.time() # same as datetime.time

# strftime (string format time)
today.strftime("%Y-%m-%d %H:%M:%S") # format the date and time
'''
%Y = year 4 digits, %y = year 2 digits
%m = month, %B = month name, %b = month abbreviation
%d = day, %A = weekday, %a = weekday abbreviation
%H = hour 24h, %I = hour 12h, %p = AM/PM
%M = minute
%S = second
'''
# datetime create like this are naive, meaning it doesn't have timezone info

# strptime (string parse time)
datetime.datetime.strptime("2024-02-24", "%Y-%m-%d") # parse the string into datetime
# string, format -> naive datetime object

# timedelta
now = datetime.datetime.now()
datetime.timedelta(days=365, weeks=5, hours=2, minutes=3) # create a timedelta object using keyword arguments
datetime.timedelta(2,0,0,0,0,3,1) # days, seconds, microseconds, milliseconds, minutes, hours, weeks
now + datetime.timedelta(days=365, weeks=5, hours=2, minutes=3)
# timedelta can be added or subtracted from datetime
# the result is also a datetime object

# create a datetime object
birthday = datetime.datetime(2024,6,28,00,00,00,00) # year, month, day, hour, minute, second
dayuntil = (birthday-today).days # timedelta object can be accessed just like datetime object




# Basic Calendar
cal = calendar.monthcalendar(2024, 2) # calendar as a python list of list (matrix)
# [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 0, 0, 0]]
# starts from Monday
cal[0] # first week
cal[0][calendar.MONDAY] # what day of month is Monday in the first week
# if it's 0, it's not in this week

for i in cal: # iterate through all the weeks
    if i[calendar.MONDAY] != 0: # if Monday is in this week (when the day of month is not 0)
        print(f'Feburuary {i[calendar.MONDAY]}, ')
