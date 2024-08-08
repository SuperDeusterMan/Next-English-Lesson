import time
from datetime import datetime, timedelta
import os

#Tells you how many seconds from Monday 12am of a week unless next lesson on a day
scheduleEnox = (137100, 137100, 213480, 377700, 377700, 741900, 741900)

##################################################################
#ChatGPT-Generation Function

def unix_time_to_human(unix_time):
    current_time = time.time()
    time_difference = unix_time - current_time
    
    if time_difference < 0:
        time_difference = abs(time_difference)
        days = int(time_difference / (60 * 60 * 24))
        hours = int(time_difference / (60 * 60)) % 24
        minutes = int(time_difference / 60) % 60
        seconds = int(time_difference) % 60
        
        time_parts = []
        if days > 0:
            time_parts.append(f"{days} days")
        if hours > 0:
            time_parts.append(f"{hours} hours")
        if minutes > 0:
            time_parts.append(f"{minutes} minutes")
        if seconds > 0:
            time_parts.append(f"{seconds} seconds")
        
        return ", ".join(time_parts) + " ago"
    else:
        days = int(time_difference / (60 * 60 * 24))
        hours = int(time_difference / (60 * 60)) % 24
        minutes = int(time_difference / 60) % 60
        seconds = int(time_difference) % 60
        
        time_parts = []
        if days > 0:
            time_parts.append(f"{days} days")
        if hours > 0:
            time_parts.append(f"{hours} hours")
        if minutes > 0:
            time_parts.append(f"{minutes} minutes")
        if seconds > 0:
            time_parts.append(f"{seconds} seconds")
        
        if time_parts:
            return "In " + ", ".join(time_parts)
        else:
            return "Now"

##################################################################

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    #this part of the code will generate the monday of the week in Unix Time
    now = datetime.now()
    monday = now - timedelta(days = now.weekday())
    monday = monday.replace(hour=0, minute=0, second = 0, microsecond = 0)
    monday = int(time.mktime(monday.timetuple()))

    #First get current unix time
    currentUnix = int(time.mktime(now.timetuple()))

    #Then get today's day of the week.
    weekday = now.weekday()

    #Add the value for today's day in the week to Monday's Unix Time. This will be when the lesson is.
    possibleLesson = monday + scheduleEnox[weekday]

    # If the time for the lesson isn't gone (meaning added value is more the current time in unix), return the added value.
    #If the time for lesson is gone (meaning less than or equal to the current time), take the next day's dictionary value, add it to Monday's Unix Time and return that value.

    if possibleLesson <= currentUnix:
        possibleLesson = monday + scheduleEnox[weekday+1]
        
    print(f'Next Lesson in at Unix Time: {possibleLesson}')
    print(f'Next Lesson: {unix_time_to_human(possibleLesson)}')

    time.sleep(1)
