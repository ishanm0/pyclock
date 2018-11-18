import sys
import datetime
import time
from time_class import current_time

try:
    command = sys.argv[1].lower()
except IndexError:
    print("I'm sorry, you didn't enter a function.")
    sys.exit(0)

current_time = current_time()

year = current_time.year
month = current_time.month
day = current_time.day
weekday = current_time.weekday
hour = current_time.hour
minute = current_time.minute
second = current_time.second

if command == 'time':
    print('It\'s {}:{}:{}.'.format(hour, minute, second))
elif command == 'date':
    print('It\'s {}, {} {}, {}.'.format(weekday, month, day, year))
elif command == 'timer':
    minutes = int(input('How long do you want the timer? (In minutes)\n'))
    while minutes > 1:
        print('{} minutes left.'.format(minutes))
        minutes -= 1
        time.sleep(60)
    print('1 minute left.')
    time.sleep(60)
    print('Your timer is done.')
elif command == 'alarm':
    alarm_time = input('What time do you want the alarm for?\n')
    split_time = alarm_time.split(':')
    alarm_hour = int(split_time[0])
    alarm_minute = int(split_time[1])
    while True:
        current_time.update()
        #current_second = int(datetime.datetime.now().second)
        current_second = int(current_time.second)
        if current_second == 0:
            #current_hour = int(datetime.datetime.now().hour)
            current_hour = int(current_time.hour)
            #current_minute = int(datetime.datetime.now().minute)
            current_minute = int(current_time.minute)
            if (alarm_hour - current_hour == 0) and (alarm_minute - current_minute == 0):
                print('Your alarm is set to now.')
                sys.exit()
            else:
                if (alarm_hour - current_hour) < 0:
                    temp_hour = current_hour + 24
                else:
                    temp_hour = current_hour
                if (alarm_minute - current_minute) < 0:
                    temp_minute = current_minute + 60
                else:
                    temp_minute = current_minute
                hour_diff = alarm_hour - temp_hour
                minute_diff = alarm_minute - temp_minute
                if hour_diff == 0:
                    print('{} minutes left.'.format(minute_diff))
                elif minute_diff == 0:
                    print('{} hours left.'.format(hour_diff))
                else:
                    print('{} hours and {} minutes left.'.format(hour_diff, minute_diff))
else:
    print("I'm sorry, that's not a recognized function.")

