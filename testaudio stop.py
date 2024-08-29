import pyttsx3
import keyboard

engine = pyttsx3.init()


def onWord(name, location, length):
    print('word', name, location, length)
    if keyboard.is_pressed("esc"):
        engine.stop()


engine.connect('started-word', onWord)

engine.say('hellojghfxdhjkjvcxvfgchxjbkldms;ljhggkljhgfghjklkjhgfhjkjh')
engine.runAndWait()
