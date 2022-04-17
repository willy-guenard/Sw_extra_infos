from PIL import Image
import d3dshot
from runeClass import Rune

###### get screanshot
# d = d3dshot.create(capture_output="numpy")
# d.display = d.displays[1]  # si besoin de le trouver sur une fenetre specifique
# d.screenshot()
# d.screenshot_to_disk(file_name="./sw-rune-efficience/Stock_image/windows.png")

# show images
imageWindow = Image.open("./sw-rune-efficience/Stock_image/windows.png")

# recuperation taille fenetre rune
rune_image = imageWindow.crop((1450, 30, 2485, 705))
runeCheck = Rune(rune_image)

# rune_image.show()
runeCheck.showRune()