import sys
import datetime
import time

try:
    command = sys.argv[1].lower()
except IndexError:
    print("I'm sorry, you didn't enter a function.")
    sys.exit(0)

month_dict = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}
week_dict = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}
year = datetime.datetime.now().year
month = month_dict[datetime.datetime.now().month]
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
weekday = week_dict[datetime.datetime.now().weekday()]

if command == 'time':
    print("It's {}:{}:{}.".format(hour, minute, second))
elif command == 'date':
    print("It's {}, {} {}, {}.".format(weekday, month, day, year))
elif command == 'timer':
    minutes = int(input("How long do you want the timer? (In minutes)\n"))
    while minutes > 1:
        print("{} minutes left.".format(minutes))
        minutes -= 1
        time.sleep(60)
    print("1 minute left.")
    time.sleep(60)
    print("Your timer is done.")
else:
    print("I'm sorry, that's not a recognized function.")