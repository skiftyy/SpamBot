import pyautogui, time

#Presets Advance
#Change path for different scripts
bee = open("C:\\Users\\26495\\OneDrive - Brisbane Boys' College\\School\\Coding\\GitHub Repository\\SpamBot\\Scripts\\beemovie.txt", 'r')
gangnam = open("C:\\Users\\26495\OneDrive - Brisbane Boys' College\School\Coding\GitHub Repository\SpamBot\\Scripts\\gangnam.txt", 'r')
pra = open("C:\\Users\\26495\OneDrive - Brisbane Boys' College\School\Coding\GitHub Repository\SpamBot\Scripts\\PRA.txt", 'r')
cars = open("C:\\Users\\26495\OneDrive - Brisbane Boys' College\School\Coding\GitHub Repository\SpamBot\Scripts\\Cars 2.txt", 'r')
y = open("C:\\Users\\26495\OneDrive - Brisbane Boys' College\School\Coding\GitHub Repository\SpamBot\Scripts\\PRA.txt", 'r')
z = open("C:\\Users\\26495\OneDrive - Brisbane Boys' College\School\Coding\GitHub Repository\SpamBot\Scripts\\PRA.txt", 'r')

#Application
teams = 0.5
xbox = 0.5
winword = 0
whatsapp = 0
instagram = 0
discord = 1

#Spammer
time.sleep(5)
#Change variable to chosen option
for word in cars:
    pyautogui.typewrite(word)
    time.sleep(winword)
    #pyautogui.press("enter")
pyautogui.press("enter")
