from PIL import Image
from Rune.screanToText import filterStat
import re
import d3dshot


class Rune:
        def __init__(self, imageRuneWindow):
            titleRune = filterStat(imageRuneWindow, 160, 45, 875, 110)

            self.typeRune = Rune.setTypeRune(titleRune)
            self.slotRune = Rune.setSlotRune(titleRune)
            self.nbUpgradeRune = Rune.setUpgradeRune(imageRuneWindow)

            mainStatData = Rune.isolatedSubStat(filterStat(imageRuneWindow, 250, 150, 600, 200))
            self.mainStatTypeRune = mainStatData[0]
            self.mainStatRune = mainStatData[1]

            initStatData = Rune.isolatedSubStat(filterStat(imageRuneWindow, 250, 220, 600, 275))
            self.initStatTypeRune = initStatData[0]
            self.initStatRune = initStatData[1]
            self.initStatRating = Rune.setRate(initStatData[0], initStatData[1])

            firstStatData = Rune.isolatedSubStat(filterStat(imageRuneWindow, 30, 300, 500, 370))
            self.firstStatTypeRune = firstStatData[0]
            self.firstStatRune = firstStatData[1]
            self.firstStatRating = Rune.setRate(firstStatData[0], firstStatData[1])

            secondeStatData = Rune.isolatedSubStat(filterStat(imageRuneWindow, 30, 360, 500, 415))
            self.secondeStatTypeRune = secondeStatData[0]
            self.secondeStatRune = secondeStatData[1]
            self.secondeStatRating = Rune.setRate(secondeStatData[0], secondeStatData[1])

            threeStatData = Rune.isolatedSubStat(filterStat(imageRuneWindow, 30, 415, 500, 475))
            self.threeStatTypeRune = threeStatData[0]
            self.threeStatRune = threeStatData[1]
            self.threeStatRating = Rune.setRate(threeStatData[0], threeStatData[1])

            fourStatData = Rune.isolatedSubStat(filterStat(imageRuneWindow, 30, 470, 500, 525))
            self.fourStatTypeRune = fourStatData[0]
            self.fourStatRune = fourStatData[1]
            self.fourStatRating = Rune.setRate(fourStatData[0], fourStatData[1])

        def getUpgradeRune(self):
            return self.nbUpgradeRune

        def getTypeRune(self):
            return self.typeRune

        def getSlotRune(self):
            return self.slotRune

        def getMainStatRune(self):
            return (self.mainStatTypeRune, self.mainStatRune)

        def getInitStatRune(self):
            return (self.initStatTypeRune, self.initStatRune)

        def getRating(self):
            return round(float(self.firstStatRating) + float(self.secondeStatRating) + float(self.threeStatRating) + float(self.fourStatRating), 2)

        def getInitSubStat(self):
            return (self.initStatTypeRune, self.initStatRune, self.initStatRating)

        def getFirstSubStat(self):
            return (self.firstStatTypeRune, self.firstStatRune, self.firstStatRating)

        def getSecondeSubStat(self):
            return (self.secondeStatTypeRune, self.secondeStatRune, self.secondeStatRating)

        def getThreeSubStat(self):
            return (self.threeStatTypeRune, self.threeStatRune, self.threeStatRating)

        def getFourSubStat(self):
            return (self.fourStatTypeRune, self.fourStatRune, self.fourStatRating)

        def setTypeRune(textRune):
            stockType = ("ENERGIE", "GARDIAN", "RAPIDE", "LAME", "RAGE", "FOCUS", "ENDURANCE", "FATALE", "DESESPOIR", "VAMPIRE", "VIOLENTE", "NEMESIS", "VOLONTE", "PROTECTION", "VENGEANCE", "DESTRUCTION", "COMBAT" "DETERMINATION", "AMELIORATION", "PRECISION", "TOLERANCE")
            
            for type in stockType:
                typeRuneCheck = textRune.find(type)
                if typeRuneCheck != -1:
                    typeRune = type
                    break
            return typeRune
        
        def setSlotRune(textRune):
            toSearch = textRune[textRune.find('(')+1:textRune.find(')')]
            return toSearch

        def setUpgradeRune(imageRuneWindow):
            textRune = filterStat(imageRuneWindow, 125, 240, 200, 280)
            return re.findall(r'[1-9]+', textRune)

        def isolatedSubStat(textRune):
            print(textRune)
            checkPoucentStat = textRune.find('%')
            textRune = re.sub(r"\s+", "", textRune)
            splitStat = textRune.split('+')
            splitStat[1] = re.findall(r'[0-9]+', splitStat[1])

            if (checkPoucentStat == -1) and (splitStat[0] == "ATK") or (splitStat[0] == "DEF") or (splitStat[0] == "HP"):
                splitStat[0] = "+" + splitStat[0]
            return splitStat

        def setRate(type, stat):
            stat = int(stat[0])
            match type:
                case "VIT":
                    rating = round(stat / 6, 2)
                case "TXCRITIG":
                    rating = round(stat / 6, 2)
                case "HP": 
                    rating = round(stat / 8, 2)
                case "ATK": 
                    rating = round(stat / 8, 2)
                case "DEF": 
                    rating = round(stat / 8, 2)
                case "PRECISION": 
                    rating = round(stat / 8, 2)
                case "RES": 
                    rating = round(stat / 8, 2)
                case "DGTSCRITIG": 
                    rating = round(stat / 7, 2)
                case "+HP": 
                    rating = round(stat / 375, 2)
                case "+ATK": 
                    rating = round(stat / 20, 2)
                case "+DEF": 
                    rating = round(stat / 20, 2)
                case _:
                    rating = 0
        
            return rating