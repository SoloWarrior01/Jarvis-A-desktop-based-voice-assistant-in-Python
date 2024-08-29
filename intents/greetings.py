"""THIS FUNCTION WILL GIVE OUTPUT OF GREETING JUST BY CALLING THE CLASS
    THE CLASS TAKES VARIABLE ONLY GREETING AND RETURNS THE GREET RESPONSE"""


class Greeting:

    input = ["jarvis", "wake up jarvis", "hello jarvis", "hi jarvis", "rise up jarvis", "hello",
             "come up jarvis", "hey jarvis", "good morning jarvis", "good evening jarvis", "good afternoon jarvis"]

    output = ["hello sir, how can i help you", "always at your service sir", "hello sir", "hello sir",
              "at your service sir", "always for you sir", "hello sir", "good morning sir",
              "good evening sir", "good afternoon sir"]

    def __init__(self, voice_command):
        self.voice_command = voice_command
        self.greet = self.response_to_greet()

    def response_to_greet(self):
        flag = ''
        if self.voice_command != '':
            for key in range(0, len(self.input)):
                if self.voice_command in self.input[key]:
                    # print(self.voice_command)
                    print(key)
                    flag = key
                    break
        else:
            pass
        try:
            response = self.output[flag]
            # print(response)
            return response
        except:
            pass

    def __repr__(self):
        return self.greet


if __name__ == '__main__':
    i = Greeting('hello jarvis')  # config=read_config()
    print(i)
