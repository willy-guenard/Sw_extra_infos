from PIL import Image
from Rune.runeClass import Rune
from Rune.windowsRune import showWindows
from Rune.screanshotgames import getRuneShow

# detailleRune = ("Type", "Slot", "Upgrade", "Main Stat", "Init Stat", "1 Sub Stat", "2 Sub Stat", "3 Sub Stat", "4 Sub Stat")

def getDataToRune():
    
    imageWindow = getRuneShow()

    # test images
    imageWindow = Image.open('.\Stock_image\windows.png')

    # recuperation taille fenetre rune
    rune_image = imageWindow.crop((1450, 30, 2485, 705)) # possition top right


    runeData = Rune(rune_image)
    showWindows(runeData)


