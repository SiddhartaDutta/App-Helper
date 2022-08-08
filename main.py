import speech_recognition as sr
import os
from pathlib import Path

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

            exeName = text + ".exe"

            #print('Spliced Read: {}'.format(text))
            
            # Attempt to launch .exe file from "Program Files (x86)"
            try:

                # Change directory to guessed subdir of "Program Files (x86)"
                pathToProgramFiles = "C:/Program Files (x86)"
                pathToProgramFiles += "/" + text

                os.chdir(pathToProgramFiles)

                # Launch .exe file
                os.startfile(exeName)

                # Print confirmation message
                print('Opening {}...'.format(exeName))

            except:
                print('Error: Folder not found.')
                print('\tAttempted Path: {}'.format(pathToProgramFiles))

            # Pathlib module search
            try:

                # Search from start of primary drive
                search_path = Path('C:/')

                print('Searching system...')
                for file in search_path.glob('**/*'):
                    if file.name == exeName:

                        # Launch .exe file
                        os.startfile(file.absolute())

                        # Print confirmation messge
                        print('Opening {}...'.format(exeName))
                        #print(f'File Found = {file.absolute()}')

                        break

            except:
                print('Error: File "{}" not found in system.'.format(exeName))

        else:
            print('Error: No \"open\" command found.')

    except:
        print('Error: Speech not understood.')