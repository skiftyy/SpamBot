import pyautogui, time

#Presets Simple Letter by Letter
#O_O = "Oh.yeah.gamers"
j = "Alistair.Nicol.is.a.beautiful.human.being"
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
bee = open("C:\\Users\\Scott Kift\\Desktop\\Code\\Spam Bot\\Scripts\\beemovie.txt", 'r')
gangnam = open("C:\\Users\\Scott Kift\\Desktop\\Code\\Spam Bot\\Scripts\\gangnam.txt", 'r')
pra = open("C:\\Users\\Scott Kift\\Desktop\\Code\\Spam Bot\\Scripts\\PRA.txt", 'r')
x = open("C:\\Users\\Scott Kift\\Desktop\\Code\\Spam Bot\\Scripts\\PRA.txt", 'r')
y = open("C:\\Users\\Scott Kift\\Desktop\\Code\\Spam Bot\\Scripts\\PRA.txt", 'r')
z = open("C:\\Users\\Scott Kift\\Desktop\\Code\\Spam Bot\\Scripts\\PRA.txt", 'r')

#Spammer
time.sleep(5)
#Change variable to chosen option
for word in gangnam:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
