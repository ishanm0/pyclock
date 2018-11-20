import sys
import datetime
import time
from time_class import current_time
import tkinter as tk
from tkinter import *

current_time = current_time()

year = current_time.year
month = current_time.month
day = current_time.day
weekday = current_time.weekday
hour = current_time.hour
minute = current_time.minute
second = current_time.second

def time_update():
	current_time.update()

	year = current_time.year
	month = current_time.month
	day = current_time.day
	weekday = current_time.weekday
	hour = current_time.hour
	minute = current_time.minute
	second = current_time.second
    
	return 'It\'s {}:{}:{} on {}, {} {}, {}.'.format(hour, minute, second, weekday, month, day, year)

hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

root = tk.Tk()

root.geometry('300x50')
root.resizable(width=False, height=False)

time = tk.Label(root, text=time_update())
time.grid()

def update_text():
	time['text'] = time_update()
	
	root.after(1000, update_text)

root.after(1, update_text)

root.mainloop()