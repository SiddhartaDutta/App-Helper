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

        if "open" in text:

            # Modify string to just open command
            appIndex = text.find('open')
            text = text[(appIndex + 5):]

            print('Spliced Read: {}'.format(text))
            
            # Attempt to launch exe file
            try:

                # Change directory to guessed subdir of "Program Files (x86)"
                pathToProgramFiles = "C:/Program Files (x86)"
                pathToProgramFiles += "/" + text

                print(pathToProgramFiles)
                os.chdir(pathToProgramFiles)

                s=os.getcwd()
                print(s)

            except:
                print('Error: File not found.')

        else:
            print('No open command found.')

    except:
        print('Not understood')