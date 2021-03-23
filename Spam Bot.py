import pyautogui, time

#Presets Simple Letter by Letter
#O_O = "Oh.yeah.gamers"
j = "Lord.Fisher.is.a.beautiful.human.being"
k = ""
l = ""
m = ""
n = ""

#Presets Simple Word by Word
#AAA = ["poop", "bum", "lol"]
a = []
b = []
c = []
d = []
e = []

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
for word in gangnam:
    pyautogui.typewrite(word)
    time.sleep(teams)
    #pyautogui.press("enter")
pyautogui.press("enter")
