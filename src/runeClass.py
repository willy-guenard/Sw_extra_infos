from PIL import Image
import pytesseract

class Rune:
        def __init__(self, imageRuneWindow):

            self.typeRune = filterStat(imageRuneWindow, 160, 45, 875, 110)
            self.slotRune = filterStat(imageRuneWindow, 160, 45, 875, 110)
            self.nbUpgradeRune = filterStat(imageRuneWindow, 125, 240, 200, 280) #mettre un double check avec images
            self.mainStatRune = filterStat(imageRuneWindow, 250, 150, 600, 200)
            self.initStatRune = filterStat(imageRuneWindow, 250, 220, 600, 275)
            self.firstStatRune = filterStat(imageRuneWindow, 30, 300, 500, 370)
            self.secondeStatRune = filterStat(imageRuneWindow, 30, 360, 500, 415)
            self.threeStatRune = filterStat(imageRuneWindow, 30, 415, 500, 475)
            self.fourStatRune = filterStat(imageRuneWindow, 30, 470, 500, 525)

        def showRune(self):
            print(self.typeRune)
            print(self.slotRune)
            print(self.nbUpgradeRune)
            print(self.mainStatRune)
            print(self.initStatRune)
            print(self.firstStatRune)
            print(self.secondeStatRune)
            print(self.threeStatRune)
            print(self.fourStatRune)


def filterStat(imageRuneWindow, left, top, right, bottom): #mettre un double check avec images
    imageFocus = imageRuneWindow.crop((left, top, right, bottom))
    textFound = pytesseract.image_to_string(imageFocus, lang='fra+eng')
    return textFound