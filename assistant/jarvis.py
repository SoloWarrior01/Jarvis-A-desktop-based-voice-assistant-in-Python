import speech_recognition as sr
import threading
from tkinter import *
import urllib.request
import os

from utils.utils import Utils
from intents.greetings import Greeting
from intents.applications import Applications
from intents.websearch import Search
from intents.games import Games
from intents.directions import Directions
from intents.calender import Calendar
from intents.reminder_timer import Reminder
from intents.alarmclock import AlarmClock
import intents.date_time as dt
from intents.calculator import Calculator


class Jarvis:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()
        threading.Thread(target=self.run()).start()

    def run(self):
        global voice_list
        speech = Utils(logger=self.logger)
        while True:
            config_check = ''
            voice_note = ''
            try:
                urllib.request.urlopen('http://google.com')
                voice_note = speech.read_voice_cmd()
                # voice_note = 'show me some games'
                voice_note = voice_note.lower()
                voice_list = voice_note.split(' ')

            except:
                # voice_note = self.No_internet()
                voice_note = voice_note.lower()
                voice_list = voice_note.split(' ')

            if 'calender' in voice_list:
                if 'show' in voice_list:
                    print('showing calender..')
                    child = Tk()
                    child.geometry('320x500')
                    child.configure(bg='black')
                    child.iconbitmap('intents/schedule.ico')
                    Calendar(child)
                    child.mainloop()
                else:
                    pass
            elif 'calculator' and 'open' in voice_list:
                root = Tk()
                b = Calculator(root)
                root.title("Simple Scientific Calculator")
                root.geometry("650x490+50+50")
                root.resizable(False, False)
                root.mainloop()
                continue

            elif 'today' in voice_list:
                if 'date' in voice_list:
                    dateday = dt.date_day()
                    Utils.speak('today is {}, {}'.format(dateday[0], dateday[1]))
                elif 'day' in voice_list:
                    dateday = dt.date_day()
                    Utils.speak('today is {}'.format(dateday[1]))
                else:
                    pass

            elif ('time' and 'now') in voice_list:
                dt.time_now()
                print('time')

            elif 'day' in voice_list:
                if 'on' in voice_list:
                    print('born')
                    lst = voice_note.split(" on ")
                    date = lst[1]
                    date = date.split(" ")
                    date[0] = date[0].rstrip('thstndr')
                    if len(date[0]) == 1:
                        date[0] = '0' + date[0]
                    date_string = date[0] + ' ' + date[1] + ' ' + date[2]
                    day_output = dt.findDay(date_string)
                    Utils.speak(day_output)
                else:
                    pass

            else:
                pass

            for i in self.config:
                for j in i:
                    check_in_config = Utils.match_pattern(voice_note, j)
                    if check_in_config:
                        config_check = i[0]

            print(config_check)

            if config_check == "intent_greeting":
                greet = Greeting(voice_command=voice_note)
                print(greet)

                if greet:
                    Utils.speak(greet)

            elif config_check == "intent_applications":
                response = Utils.random_choice(self.config[2][1:])
                Applications(logger=self.logger, response=response, command=voice_note)

            elif config_check == "intent_web_search":
                search = Search(logger=self.logger, config=self.config)
                result = search.run(voice_note)
                if result:
                    pass
                else:
                    pass

            elif config_check == "intent_screensaver":
                off_screen = Utils.random_choice(self.config[5])
                self.logger.info('Screensaver on: {}'.format(off_screen))
                os.startfile(off_screen)

            elif config_check == "intent_games":
                class_game = Games(logger=self.logger)
                game = class_game.run(voice_note)
                self.logger.info('Games: {}'.format(game))

            elif config_check == "intent_shutdown":
                Utils.speak('connecting to command prompt')
                Utils.speak('shutting out your computer')
                self.logger.info('Shutting Down PC')
                # os.system('shutdown -s')

            elif config_check == "intent_quit":
                Utils.speak('bye sir, have a nice day')
                Utils.speak('closing all systems')
                self.logger.info('Turning off Program')
                # quit()

            elif config_check == "intent_directions":
                location = Directions(logger=self.logger)
                output = location.run(voice_note)
                if not output:
                    self.logger.info('{}: {}'.format(output[0], output[1]))
                    pass
                else:
                    pass

            elif config_check == "intent_remainder":
                reminder = Reminder(logger=self.logger)
                output = reminder.reminder(voice_note)
                if output != True:
                    self.logger.info('{}'.format(output))
                    pass
                else:
                    pass

            elif config_check == "intent_alarm":
                alarm = AlarmClock(logger=self.logger)
                output = alarm.run(voice_note)
                if output:
                    pass
                else:
                    pass

            break
