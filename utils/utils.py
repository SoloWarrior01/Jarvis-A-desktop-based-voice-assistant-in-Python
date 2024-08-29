import pyttsx3
import random
import speech_recognition as sr


class Utils:
    def __init__(self, logger):
        self.logger = logger
        self.speech = sr.Recognizer()

    def read_voice_cmd(self):
        voice_input = ''
        try:

            with sr.Microphone() as source:
                print('listening...')
                audio = self.speech.listen(source=source, timeout=5, phrase_time_limit=5)
            voice_input = self.speech.recognize_google(audio)
            self.logger.info('Input: {}'.format(voice_input))

        except sr.UnknownValueError:
            print('google speech recognition could not understand audio')
            pass
        except sr.RequestError:
            print('network error')

        except sr.WaitTimeoutError:
            pass
        except TimeoutError:
            pass

        return voice_input.lower()



    @staticmethod
    def match_pattern(voice_note, pattern):
        if (pattern+" ") in voice_note:
            return True
        else:
            return False

    @staticmethod
    def speak(response):
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.say(response)
            engine.runAndWait()
        except ImportError:
            print('driver not found')
        except RuntimeError:
            print('driver fails to initialise')

    @staticmethod
    def random_choice(response):
        return random.choice(response)

    @staticmethod
    def stop_speak():
        engine.stop()