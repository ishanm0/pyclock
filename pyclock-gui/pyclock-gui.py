import sys
import datetime
import time
from time_class import current_time
from guizero import App, PushButton, ListBox, Text, TextBox

app = App(title="pyclock")

current_time = current_time()

year = current_time.year
month = current_time.month
day = current_time.day
weekday = current_time.weekday
hour = current_time.hour
minute = current_time.minute
second = current_time.second

hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

time = Text(app, text='{}:{}:{}'.format(hour, minute, second))
date = Text(app, text='{}, {} {}, {}.'.format(weekday, month, day, year))
timer_text = Text(app, text='How long do you want the timer? (in minutes)')
timer_minutes = TextBox(app, text='', enabled=True)
timer_button = PushButton(app, timer_minutes.disable)

def update():
    current_time.update()

    year = current_time.year
    month = current_time.month
    day = current_time.day
    weekday = current_time.weekday
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    time.value = '{}:{}:{}'.format(hour, minute, second)
    date.value = '{}, {} {}, {}.'.format(weekday, month, day, year)

time.repeat(1000, update)
date.repeat(1000, update)

app.display()