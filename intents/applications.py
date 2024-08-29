import os
import webbrowser

from utils.utils import Utils
import csv
import threading


def read_applications():
    try:
        with open('intents\\applications.csv') as file1:
            data1 = csv.reader(file1)
            listdata1 = list(data1)
            return listdata1
    except:
        Utils.speak('Sir, no application is registered with me... please give me a moment to read the applications')
        print('dir /s /b *.exe | findstr /v .exe. > {}\\intents\\applications.csv')
        Utils.speak('sir, use this in command prompt to register applications')


class Applications:
    def __init__(self, logger, response, command):
        self.logger = logger
        self.response = response
        self.command = command
        threading.Thread(target=self.launch()).start()

    def get_app_name(self):
        # 'open chrome'
        list_command = self.command.split(' ')
        # print(list_command)
        for i in range(len(list_command)):
            if list_command[i] == 'launch':
                if list_command[i+2]:
                    if list_command[i+2] != ('please'):
                        app = list_command[i+1]+' '+list_command[i+2]
                    else:
                        app = list_command[i+1]
                else:
                    app = list_command[1+1]
                return app

            elif list_command[i] == 'open':
                try:
                    if list_command[i + 2] != ('please'):
                        app = list_command[i + 1] + ' ' + list_command[i + 2]
                    else:
                        app = list_command[i + 1]
                except:
                    app = list_command[i + 1]
                return app

    def get_app_path(self):
        name = self.get_app_name()
        # print(name)
        self.logger.info('App Name: {}'.format(name))
        applications = read_applications()
        for i in applications:
            if name.lower() in i[0].lower():
                # print(i[0])
                return i[1]

    def launch(self):
        path = self.get_app_path()
        if path:
            if "http" in path:
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(path)
            else:
                os.startfile('{}'.format(path))
                Utils.speak(self.response)

        else:
            Utils.speak('sorry sir, the app which you are looking for is not registered with my database')
