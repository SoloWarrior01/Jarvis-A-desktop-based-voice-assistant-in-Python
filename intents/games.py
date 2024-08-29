from threading import Thread
import webbrowser
from utils.utils import Utils
import os
import speech_recognition as sr
from tkinter import *
import logging
from PIL import Image, ImageTk
import sys

root = None
root1 = logging.getLogger()
root1.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                              datefmt='%d-%m-%Y %H:%M:%S')
handler.setFormatter(formatter)
root1.addHandler(handler)


class Games:
    list_online = {'miniclip': 'https://miniclip.com/games/en/', 'kizi': 'https://kizi.com',
                   'arkadium': 'https://www.arkadium.com/free-online-games/',
                   'ea': 'https://www.ea.com/games/library/online'}

    list_offline = {'chess': ['C:\Program Files\Microsoft Games\Chess\Chess.exe', 'intents\games\Chess.png'],
                    'freecell': ['C:\Program Files\Microsoft Games\FreeCell\FreeCell.exe', 'intents\games\FreeCellMCE.png'],
                    'hearts': ['C:\Program Files\Microsoft Games\Hearts\Hearts.exe', 'intents\games\HeartsMCE.png'],
                    'mahjong': ['C:\Program Files\Microsoft Games\Mahjong\Mahjong.exe', 'intents\games\MahjongMCE.png'],
                    'minesweeper': ['C:\Program Files\Microsoft Games\Minesweeper\MineSweeper.exe',
                                    'intents\games\minesweeperMCE.jpg'],
                    'purple place': ['C:\Program Files\Microsoft Games\Purble Place\PurblePlace.exe',
                                     'intents\games\PurblePlaceMCE.png'],
                    'solitaire': ['C:\Program Files\Microsoft Games\Solitaire\Solitaire.exe',
                                  'intents\games\SolitaireMCE.png'],
                    'spider solitaire': ['C:\Program Files\Microsoft Games\SpiderSolitaire\SpiderSolitaire.exe',
                                         'intents\games\SpiderSolitaireMCE.png'],
                    'plant versus zombie': ['E:\\vaibhav.docx\\Plants vs. Zombies\\PlantsVsZombies.exe',
                                            'intents\games\plantsvszombies.png'],
                    'plants versus zombies': ['E:\\vaibhav.docx\\Plants vs. Zombies\\PlantsVsZombies.exe',
                                              'intents\games\plantsvszombies.png'],
                    'plants versus zombie': ['E:\\vaibhav.docx\\Plants vs. Zombies\\PlantsVsZombies.exe',
                                             'intents\games\plantsvszombies.png']}

    def __init__(self, logger):
        self.logger = logger
        self.speech = sr.Recognizer()

    def action(self, web, window):
        window.destroy()
        for i in self.list_online.keys():
            if i == web:
                link = self.list_online[i]
                chrome_dir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_dir).open(link)
                break

    def online_games(self):
        Utils.speak('choose the website you want to play in')
        Thread(target=lambda lst=self.list_online.keys(): Utils.speak(list(lst))).start()

        root = Tk()
        Label(root, text='websites', font=('algerian', 20, 'bold'), bg='orange', fg='white').pack()
        for i in list(self.list_online.keys()):
            Button(root, text=i.upper(), font=('arial', 20, 'bold'),
                   width=15, bg='DodgerBlue2', fg='white',
                   command=lambda game=i, window=root: self.action(game, window)).pack()
        Button(root, text='SEARCH WEB', font=('arial', 20, 'bold'),
               width=15, bg='DodgerBlue2', fg='white',
               command=lambda: [root.destroy(),
                                # Utils.stop_speak(),
                                Thread(target=lambda text='searching web for more games': Utils.speak(text)).start(),
                                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(
                                    'https://www.google.com/search?q=best+online+websites+gaming')]).pack()
        root.mainloop()

    def offline_button(self, game, window):
        window.destroy()
        for i in self.list_offline.keys():
            if i == game:
                path = self.list_offline[i][0]
                os.startfile('{}'.format(path))
                break

    def offline_games(self, game_input):

        # game_input = 'show'
        if game_input in self.list_offline.keys():
            os.startfile('{}'.format(self.list_offline[game_input][0]))

        elif 'show' in game_input:
            root_offline = Tk()
            root_offline.resizable(False, False)
            root_offline.geometry('818x623')
            root_offline.title = 'offline games'

            fullcanvas = Canvas(root, height='623', width='818', bd=0, highlightthickness=0, relief='raised',
                                bg='black')
            fullcanvas.pack()

            copy_of_image1 = Image.open(r"intents\\images\offline_games_background.jpg")
            img1 = ImageTk.PhotoImage(copy_of_image1)

            fullcanvas.create_image(40, 312, image=img1)
            count_x = 0

            x = 75
            y = 50
            # image = [0 for image in range(len(self.list_offline.keys()) - 2)]
            for i in range(len(self.list_offline.keys()) - 2):
                if (count_x % 4 == 0) and (count_x != 0):
                    y += 180
                    x = 75
                else:
                    pass
                image = '{}'.format(list(self.list_offline.values())[i][1])
                copy_of_image = Image.open(r"{}".format(image))
                photo = ImageTk.PhotoImage(copy_of_image)

                btn = Button(root_offline, image=photo,
                             command=lambda game=list(self.list_offline.keys())[i],
                                            window=root_offline: self.offline_button(game, window))
                btn.image = photo
                btn.place(x=x, y=y)

                count_x += 1
                x += 180

            root_offline.mainloop()
            # voice_check_wants_online = Utils(logger=self.logger)

            output = ''
            count = 0
            voice_check_wants_online = Utils(logger=self.logger)
            while (output == '') and (count < 3):
                output = voice_check_wants_online.read_voice_cmd()
                count += 1

            if 'online' in output:
                root_offline.destroy()
                self.online_games()

            else:
                pass

    def run(self, query):
        query = query.split(' ')
        print(query)
        if 'online' in query:
            print('online games')
            self.online_games()

        elif 'offline' in query:
            print('offline games')
            Utils.speak('which game do you want to play?, do you have any choices or should i show some options')
            voice = Utils(logger=self.logger)
            game_input = voice.read_voice_cmd()
            print(game_input)

            if game_input == '':
                self.offline_games('show')

            elif game_input in self.list_offline.keys():
                self.offline_games(game_input)

            else:
                Utils.speak('sorry the game is not registered with me, please choose from the following ')
                self.offline_games('show')

        elif 'show' in query:
            self.offline_games('show')


if __name__ == '__main__':
    emp = Games(logger=root1)
    emp.run('show me offline games')
