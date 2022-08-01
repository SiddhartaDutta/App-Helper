import speech_recognition as sr
import os

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak anything: ')
    audio = recognizer.listen(source)

    try:

        # Convert audio to string
        text = recognizer.recognize_google(audio)
        #print('Original Read: {}'.format(text))

        if "open" in text:

            # Modify string to just open command
            appIndex = text.find('open')
            text = text[(appIndex + 5):]

            #print('Spliced Read: {}'.format(text))
            
            # Attempt to launch exe file
            try:

                # Change directory to guessed subdir of "Program Files (x86)"
                pathToProgramFiles = "C:/Program Files (x86)"
                pathToProgramFiles += "/" + text

                os.chdir(pathToProgramFiles)

                exeName = text + ".exe"
                os.startfile(exeName)

            except:
                print('Error: Folder not found.')
                print('\tAttempted Path: {}'.format(pathToProgramFiles))

        else:
            print('Error: No \"open\" command found.')

    except:
        print('Error: Speech not understood.')