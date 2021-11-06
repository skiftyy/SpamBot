import pyautogui, time

#Change path for different scripts
bee = open("C:\\GitHub\\SpamBot\\Scripts\\beemovie.txt", 'r')
gangnam = open("C:\\GitHub\\SpamBot\\Scripts\\Gangnam.txt", 'r')
pra = open("C:\\GitHub\\SpamBot\\Scripts\\PRA.txt", 'r')
cars = open("C:\\GitHub\\SpamBot\\Scripts\\Cars 2.txt", 'r')
y = open("C:\\GitHub\\SpamBot\\Scripts\\beemovie.txt", 'r')
z = open("C:\\GitHub\\SpamBot\\Scripts\\beemovie.txt", 'r')

#Applications
winword = 0
discord = 1
teams = 0.5
whatsapp = 0
instagram = 0

#Variables
script = gangnam
app = winword
start = 0
start2 = 0

while start == 0:
    print("")
    print("SCRIPT OPTIONS:")
    print("bee")
    print("gangnam")
    print("pra")
    print("cars")
    print("")
    a = input("Script: ")
    if a == "bee":
        script = bee
        start = 1
    elif a == "gangnam":
        script = gangnam
        start = 1
    elif a == "pra":
        script = pra
        start = 1
    elif a == "cars":
        script = cars
        start = 1
    else:
        start = 0

while start2 == 0:
    print("")
    print("APP OPTIONS:")
    print("word")
    print("discord")
    print("instagram")
    print("teams")
    print("whatsapp")
    print("")
    b = input("App: ")
    if b == "word":
        app = winword
        start2 = 1
    elif b == "discord":
        app = discord
        start2 = 1
    elif b == "teams":
        app = teams
        start2 = 1
    elif b == "whatsapp":
        app = whatsapp
        start2 = 1
    elif b == "instagram":
        app = instagram
        start2 = 1
    else:
        start2 = 0
        

time.sleep(5)
for word in script:
    pyautogui.typewrite(word)
    time.sleep(app)
pyautogui.press("enter")
