import time
import speech_recognition as sr
from datetime import *
import logging
import sys

from utils.utils import Utils


'''ALL NEW ADVANCED ALARM CLOCK'''


speech = sr.Recognizer()

time_terms = {'half an hour': 1800, 'an hour': 3600}
time_words = {'seconds': 1, 'minutes': 60, 'hour': 3600, 'hours': 3600}

time_final = {'o\'clock': 'hour'}

root = None
root1 = logging.getLogger()
root1.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                              datefmt='%d-%m-%Y %H:%M:%S')
handler.setFormatter(formatter)
root1.addHandler(handler)


class AlarmClock:
    def __init__(self,logger):
        self.speech = sr.Recognizer()
        self.logger = logger
        self.utils = Utils(logger=self.logger)

    def _intime_(self,voice):
        time = datetime.now()
        current_time = time.strftime("%H:%M:%S")
        print(current_time)

        time_for_alarm = voice.split(' ')
        s1 = s2 = s3 = 0
        for i in range(len(time_for_alarm)):
            # print(time_for_alarm[i])
            if time_for_alarm[i] in 'seconds':
                # print(time_for_alarm[i])
                # print(time_for_alarm[i-1])
                s1 = int(time_for_alarm[i - 1])

            elif time_for_alarm[i] in 'minutes':
                # print(time_for_alarm[i])
                # print(time_for_alarm[i-1])
                s2 = int(time_for_alarm[i - 1])

            elif time_for_alarm[i] in 'hours':
                # print(time_for_alarm[i])
                # print(time_for_alarm[i-1])
                s3 = int(time_for_alarm[i - 1])

            else:
                pass
        time_add = timedelta(hours=s3, minutes=s2, seconds=s1)
        print(time_add)
        time2 = time + time_add
        print(time2)

    def final_time_given(self, time):
        time.replace('set ', '')
        time.replace('an ', '')
        time.replace('alarm ', '')
        time.replace('for ', '')

        time_of_alarm = time.split(' ')

        s1 = s2 = s3 = 0
        for i in range(len(time_of_alarm)):
            # print(time_for_alarm[i])
            if time_of_alarm[i] in 'o\'clock':
                # print(time_for_alarm[i])
                # print(time_for_alarm[i-1])
                time_delta_form = timedelta(hours=time_of_alarm[i-1])
                s1 = int(time_of_alarm[i - 1])

            elif time_of_alarm[i] in 'minutes':
                # print(time_for_alarm[i])
                # print(time_for_alarm[i-1])
                s2 = int(time_of_alarm[i - 1])

            elif time_of_alarm[i] in 'hours':
                # print(time_for_alarm[i])
                # print(time_for_alarm[i-1])
                s3 = int(time_of_alarm[i - 1])

            else:
                pass

    def run(self, time_check):
        # time_check = self.utils.read_voice_cmd()

        voice_list = time_check.split(' ')

        print(voice_list)

if __name__ == '__main__':
    emp = AlarmClock(logger=root1)
    emp._intime_('3 hours 32 minutes 15 seconds')
