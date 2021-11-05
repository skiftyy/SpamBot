import pyautogui, time

#Presets Advance
#Change path for different scripts
bee = open("C:\\GitHub\\SpamBot\\Scripts\\beemovie.txt", 'r')
gangnam = open("C:\\GitHub\\SpamBot\\Scripts\\Gangnam.txt", 'r')
pra = open("C:\\GitHub\\SpamBot\\Scripts\\PRA.txt", 'r')
cars = open("C:\\GitHub\\SpamBot\\Scripts\\Cars 2.txt", 'r')
y = open("C:\\GitHub\\SpamBot\\Scripts\\beemovie.txt", 'r')
z = open("C:\\GitHub\\SpamBot\\Scripts\\beemovie.txt", 'r')

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
    time.sleep(winword)
    #pyautogui.press("enter")
pyautogui.press("enter")
