import d3dshot 

def getRuneShow():
    screanWindows = d3dshot.create()
    # screanWindows.display = screanWindows.displays[1]  # si besoin de le trouver sur une fenetre specifique
    screanWindows.screenshot()
    screanWindows.screenshot_to_disk(file_name="./Stock_image/windows.png")
    # return screanWindows
