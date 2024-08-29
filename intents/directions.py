import webbrowser
import urllib.request
from utils.utils import Utils
import speech_recognition as sr


class Directions:
    def __init__(self, logger):
        self.logger = logger
        self.speech = sr.Recognizer()

    @staticmethod
    def directions(location, from_where):
        weburl = urllib.request.urlopen("https://www.google.com/maps/dir/" + from_where + "/" + location)
        url = weburl.geturl()
        webbrowser.open_new(url)
        return True

    @staticmethod
    def location(location):
        weburl = urllib.request.urlopen("https://www.google.com/maps/search/" + location)
        url = weburl.geturl()
        webbrowser.open_new(url)
        return True

    def run(self, query):
        if 'where is' in query:
            place = query.split('is ')
            output = Directions.location(place[1])
            if output:
                return ['location of', place[1]]

        elif 'location of' in query:
            place = query.split('of ')
            output = Directions.location(place[1])
            if output:
                return ['location of', place[1]]

        elif 'directions to' in query:
            place = query.split('to ')[1]
            Utils.speak('please tell your current location... i am not able to get your current location')
            starting_point = ''
            count = 0
            voice = Utils(logger=self.logger)
            while (starting_point == '') and (count < 3):
                starting_point = voice.read_voice_cmd()
                count += 1
            output = Directions.directions(place, starting_point)
            if output:
                return ['Directions to ', place]

        else:
            Utils.speak('i don\'t know how to respond to that')
            return True