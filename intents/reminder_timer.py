import time
from datetime import datetime, timedelta
import logging
import sys

import speech_recognition as sr

from utils.utils import Utils

root = None
root1 = logging.getLogger()
root1.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                              datefmt='%d-%m-%Y %H:%M:%S')
handler.setFormatter(formatter)
root1.addHandler(handler)


class Reminder:
    def __init__(self, logger):
        self.logger = logger
        self.speech = sr.Recognizer()
        self.utils = Utils(logger=self.logger)

    @staticmethod
    def find_duration(time_string):
        time_list = time_string.split(' ')

        time = datetime.now()
        current_time = time.strftime("%H")
        print(current_time)
        
        for i in time_list:
            if i == 'o\'clock':
                time_duration = timedelta(hours=30)# (int(i-1) - int(current_time)))
                return time_duration

    def timer(self, time_string):  # l = list of time elements
        time_correct = 0
        l = time_string.split(' ')
        h = m = s = 0
        while time_correct == 0:
            try:
                if len(l) == 2:
                    if l[1] in ["hour", "hours"]:
                        h = int(l[0]) * 3600
                        m = 0
                        s = 0
                    elif l[1] in ["minute", 'minutes']:
                        m = int(l[0]) * 60
                        s = 0
                        h = 0
                    elif l[1] in ["second", "seconds"]:
                        s = int(l[0])
                        h = 0
                        m = 0
                elif len(l) == 4:
                    if l[1] == ["hour", 'hours']:
                        h = int(l[0]) * 3600
                        if l[3] == "minutes" or "minute":
                            m = int(l[2]) * 60
                            s = 0
                        elif l[3] == "second" or "seconds":
                            s = int(l[4])
                            m = 0
                    elif l[1] == "minutes" or "minute":
                        m = int(l[0]) * 60
                        s = int(l[2])
                        h = 0
                elif len(l) == 6:
                    h = int(l[0]) * 3600
                    m = int(l[2]) * 60
                    s = int(l[4])
                time_correct = 1
            except:
                self.utils.speak("such a format is not accepted")

            t = h + m + s
            while t > 0:
                time.sleep(1)
                t = t - 1
            return True

    def reminder(self, remind):
        remind_list = remind.split(' ')
        if 'set a reminder' in remind:
            remind_getting_time = remind.split('for ')
            if 'to' in remind_getting_time[1]:
                reminder_condition = remind_getting_time[1].split('to ')
                reminder_statement = reminder_condition[1]
                output = self.timer(reminder_condition[0])
                if output:
                    self.utils.speak('time is up, you have to {}'.format(reminder_statement))
                    self.utils.speak('time is up, you have to {}'.format(reminder_statement))
                else:
                    pass
            else:
                time = remind_getting_time[1]
                output = self.timer(time)
                if output:
                    self.utils.speak('time is up')
                    self.utils.speak('time is up')

                else:
                    pass

        elif 'remind me' in remind:
            if ('to ' and 'after') in remind_list:
                remind_getting_time = remind.split('to ')
                if 'after' in remind_getting_time[1]:
                    remind_time = remind_getting_time[1].split('after ')[1]
                    output = self.timer(remind_time)

                    if output:
                        self.utils.speak('time is up, you have to {}'.format(remind_time[0]))
                        self.utils.speak('time is up, you have to {}'.format(remind_time[0]))
                        return 'Reminder to {} after {}'.format(remind_time[0], remind_time[1])

            elif ('after' in remind_list) and ('to ' not in remind_list):
                remind_time = remind.split('after ')[1]
                output = self.timer(remind_time)

                if output:
                    self.utils.speak('time is up')
                    self.utils.speak('time is up')
                    return 'Reminder for {}'.format(remind_time)

            elif ('to ' in remind_list) and ('after' not in remind_list):
                remind_condition = remind.split('to ')[1]
                Utils.speak('sure, but please tell for how much time or at what time')

                # output = 'at 8 o\'clock'
                output = ''
                count = 0
                while (output == '') and (count < 2):
                    output = self.utils.read_voice_cmd()
                    count += 1

                if 'at' in output:
                    final_time = output.split('at ')[1]
                    time_duration = Reminder.find_duration(final_time)
                    print(time_duration)
                    return 'Reminder at {} to {}'.format(final_time, remind_condition)

                else:
                    time_duration = output
                    out = self.timer(time_duration)
                    print(out)
                    if output:
                        return 'Reminder to {} after {}'.format(remind_condition, output)
                        pass
                    else:
                        self.utils.speak('unexpected error occurred please try again')


if __name__ == '__main__':
    emp = Reminder(logger=root1)
    emp.reminder('remind me to set phone')
