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
            text = text[appIndex:]

            print('Spliced Read: {}'.format(text))
            
            # Attempt to launch exe file
            try:

                # Change directory to "Program Files (x86)"
                pathToProgramFiles = "C:/Program Files (x86)"
                os.chdir(pathToProgramFiles)

                # Change directory to requested

            except:
                print('Error: File not found.')

        else:
            print('No open command found.')

    except:
        print('Not understood')