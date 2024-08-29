import pyttsx3
from datetime import datetime
import calendar

engine = pyttsx3.init()
engine.setProperty('rate', 125)

days = {0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


def date_day():
    today = datetime.today()
    d1 = today.strftime("%d %B,%Y")  # date as-- 'dd month,yyyy'
    day = datetime.strptime(d1, '%d %B,%Y').weekday()
    return [d1, days[day]]
    # engine.say(d1)
    # engine.say('its '+ calendar.day_name[day])
    # engine.runAndWait()


def time_now():
    now = datetime.now()
    current_time = now.strftime("%H hours %M minutes") # %S seconds")
    engine.say(current_time)
    engine.runAndWait()


def findDay(date):
    born = datetime.strptime(date, '%d %B %Y').weekday()  # date as-- 'dd mm yyyy'
    return calendar.day_name[born]
