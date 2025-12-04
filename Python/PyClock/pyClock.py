#Programmer: Daniel Rojo
#Email: dcano9@cnm.edu
#Purpose: To create a simple digital clock with a gui
#python version: 3.12.7

from tkinter import *
from datetime import datetime
from zoneinfo import ZoneInfo #ZoneInfo uses tz database

#creates the main window
root = Tk()
root.title('Digital Clock')
root.geometry('500x250')

#sets the current timezone for use
current_timezone = ZoneInfo('US/Eastern')

#function that sets the time
def time():
    """Sets the time and updates it every second"""
    now = datetime.now(current_timezone)
    display_time = now.strftime('%I:%M:%S %p') #gives us a string of the time to display
    #making the label in this function will continuously print the time
    label.config(text = display_time)
    label.after(1000, time) #updates the time every second

#function to set the timezon
def set_timezone(zone):
    """Sets current_timezone with a new timezone"""
    global current_timezone #I read that global is bad practice but I couldn't find a way to do this without it
    current_timezone = ZoneInfo(zone)

#function to make the buttons and change the timezone
def timezone():
    """Creates the buttons from the timezones held in a dictionary"""
    timezones = {'Eastern':'US/Eastern',
                 'Pacific':'US/Pacific',
                 'London':'Europe/London',
                 'Moscow':'Europe/Moscow',
                 'Bangkok':'Asia/Bangkok',
                 'Tokyo':'Asia/Tokyo'}
    #creates a button for every key, uses the values to send to set_timezone
    for name, zone in timezones.items():
        button = Button(root, text = name, command = lambda t_zone = zone: set_timezone(t_zone))
        button.pack()

#keeping the labels out here allows them to update with the function
label = Label(root, font = ('georgia', 40, 'bold'))
label.pack()

time()
timezone()
root.mainloop()