import speech_recognition as sr
import os

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak anything: ')
    audio = recognizer.listen(source)

    try:

        # Convert audio to string
        text = recognizer.recognize_google(audio)
        print('Original Read: {}'.format(text))

        # Modify string to just open command
        appIndex = text.find('open')
        text = text[appIndex:]

        print('Spliced Read: {}'.format(text))

        try:

            # Change directory to "Program Files (x86)"
            #pathToProgramFiles = "C:/Program Files (x86)"
            #os.chdir(pathToProgramFiles)

            test = os.getcwd()
            print(test)

            path = "C:/Users/siddh/OneDrive/Documents/Visual Studio Code"
            os.chdir(path)
            test = os.getcwd()
            print(test)
        except:
            print('yur')

    except:
        print('Not understood')