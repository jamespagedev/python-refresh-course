"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

"""
current_month = datetime.now().strftime('%m') // 02 //This is 0 padded
current_month_text = datetime.now().strftime('%h') // Feb
current_month_text = datetime.now().strftime('%B') // February

current_day = datetime.now().strftime('%d')   // 23 //This is also padded
current_day_text = datetime.now().strftime('%a')  // Fri
current_day_full_text = datetime.now().strftime('%A')  // Friday

current_weekday_day_of_today = datetime.now().strftime('%w') //5  Where 0 is Sunday and 6 is Saturday.

current_year_full = datetime.now().strftime('%Y')  // 2018
current_year_short = datetime.now().strftime('%y')  // 18 without century

current_second= datetime.now().strftime('%S') //53
current_minute = datetime.now().strftime('%M') //38
current_hour = datetime.now().strftime('%H') //16 like 4pm
current_hour = datetime.now().strftime('%I') // 04 pm

current_hour_am_pm = datetime.now().strftime('%p') // 4 pm

current_microseconds = datetime.now().strftime('%f') // 623596 Rarely we need.

current_timzone = datetime.now().strftime('%Z') // UTC, EST, CST etc. (empty string if the object is naive).
"""

import sys
import calendar
from datetime import datetime
# Get User Input
# Precondition - 1 input must be month (with the value as a number 1-12)
print("Hint: use commas to seperate arguments")
userInput = input("Enter arg(s) or hit enter for none: ").split(',')

# If user entered nothing, print current month
try:
    if (userInput[0] == ''):
        print(calendar.month(datetime.now().year, datetime.now().month))
    elif (len(userInput) == 1):  # If user entered 1 arg, assume it was month
        # Precondition - year = ####, month = 1-12
        if (int(userInput[0]) > 0 and int(userInput[0]) < 13):
            print(calendar.month(datetime.now().year, int(userInput[0])))
        else:
            print('invalid input: must provide a single integer between 1-12')
    elif (len(userInput) == 2):  # If user entered 2 args, assume it was month and year
        # Precondition - year = ####, month = 1-12
        if (int(userInput[0]) > 0):
            print(calendar.month(int(userInput[1]), int(userInput[0])))
        else:
            print('invalid input: must provide month and year(e.g.: 3,2011)')
except ValueError:
    print('invalid input: must provide 0-2 arguments as numbers only')