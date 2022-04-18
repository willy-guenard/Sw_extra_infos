import pytesseract
import unicodedata
import re

def filterStat(imageRuneWindow, left, top, right, bottom): #mettre un double check avec images
    imageFocus = imageRuneWindow.crop((left, top, right, bottom))
    textFound = pytesseract.image_to_string(imageFocus, lang='fra+eng', config=r'--psm 4 --oem 3')

    textFound = textFound.upper()
    textFound = strip_accents(textFound)
    textFound = re.sub(r'[.]+', '', textFound)
    print(textFound)
    return textFound


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
    if unicodedata.category(c) != 'Mn')