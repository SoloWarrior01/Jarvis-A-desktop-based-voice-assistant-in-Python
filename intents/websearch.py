import csv
import webbrowser
import speech_recognition as sr
from googlesearch import search
from utils.utils import Utils


def read_websearch():
    with open('intents\\websearch.csv') as f:
        data = csv.reader(f)
        listdata = list(data)

        return listdata


class Search:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()

    def is_valid_google_search(self, to_be_searched):
        for i in to_be_searched.split(' '):
            if i in self.config[3]:
                return True

    @staticmethod
    def search_for_me(query):
        j = search(query, num_results=3, advanced=True)
        data_from_urls = []
        for k in j:
            data_from_urls.append(k.description)
        return data_from_urls

    def google_search_result(self, query):
        if self.is_valid_google_search(query):
            self.logger.info('Web Search : {}'.format(query))

            search_result = self.search_for_me(query)

            for i in search_result:
                print(i)
            Utils.speak("Top result" + search_result[0])
            Utils.speak("Do you want me to show you?")
            show = Utils(logger=self.logger)
            show_on_chrome = show.read_voice_cmd()
            if 'show' in show_on_chrome:
                webbrowser.open('https://www.google.com/search?q={}'.format(query))
                return True
            else:

                return True

    @staticmethod
    def is_which_search(query):
        questions = read_websearch()
        for i in questions:
            for j in i:
                if j in query:
                    return i[0]
                else:
                    pass
        else:
            return 'search web'

    def run(self, query):
        output = self.is_which_search(query=query)
        print(output)
        if output == 'search web':
            webbrowser.open('https://www.google.com/search?q={}'.format(query))

        elif output == 'speak_out':
            result = self.google_search_result(query)
            if result:
                return True

        else:
            query = query.replace("search ", "", 2)
            query = query.replace("for", "", 2)
            # print(statement)
            webbrowser.open('https://www.google.com/search?q={}'.format(query))
            return True
