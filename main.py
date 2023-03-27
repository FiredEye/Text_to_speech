import os

# if __name__ == "__main__":
#     print("Welcome to the future: ")
#     say = input("Enter words to hear its harmony: ")
#     command = f''' PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{say}');"'''
#     os.system(command)

def robo_speak():
    print("Welcome to the future: ")
    # ask_user = input("Are you lonely? Want to speak with Robo_speak:[Y/N] ").lower()

    # while ask_user == "y":
    #     say = input("Enter words to hear its harmony: ")
    #
    #     command = f''' PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{say}');"'''
    #     os.system(command)
    #     ask_user = input("Want to speak with Robo_speak again:[Y/N] ").lower()
    #
    # print("Thanks for using my feature!!")

    while True:
        say = input("Enter words to hear it's harmony: ")
        if say == 'q':
            os.system(''' PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye friend  see you again');"''')
            break
        command = f''' PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{say}');"'''
        os.system(command)


    print("Thanks for using my feature!!")

robo_speak()