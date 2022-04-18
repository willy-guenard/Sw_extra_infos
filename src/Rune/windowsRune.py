
from tkinter import *
from tkinter import ttk

def showWindows(runeData):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Label(frm, text=runeData.getUpgradeRune()).grid(column=0, row=0)
    ttk.Label(frm, text=runeData.getTypeRune()).grid(column=1, row=0)
    ttk.Label(frm, text=runeData.getSlotRune()).grid(column=2, row=0)

    ttk.Label(frm, text=runeData.getMainStatRune()).grid(column=0, row=1)
    ttk.Label(frm, text=runeData.getInitStatRune()).grid(column=1, row=1)
    ttk.Label(frm, text=runeData.getRating()).grid(column=2, row=1)

    firststat = runeData.getFirstSubStat()
    ttk.Label(frm, text=firststat[0]).grid(column=0, row=2)
    ttk.Label(frm, text=firststat[1]).grid(column=1, row=2)
    ttk.Label(frm, text=firststat[2]).grid(column=2, row=2)

    secondestat = runeData.getSecondeSubStat()
    ttk.Label(frm, text=secondestat[0]).grid(column=0, row=3)
    ttk.Label(frm, text=secondestat[1]).grid(column=1, row=3)
    ttk.Label(frm, text=secondestat[2]).grid(column=2, row=3)

    threeStat = runeData.getThreeSubStat()
    ttk.Label(frm, text=threeStat[0]).grid(column=0, row=4)
    ttk.Label(frm, text=threeStat[1]).grid(column=1, row=4)
    ttk.Label(frm, text=threeStat[2]).grid(column=2, row=4)

    fourStat = runeData.getFourSubStat()
    ttk.Label(frm, text=fourStat[0]).grid(column=0, row=5)
    ttk.Label(frm, text=fourStat[1]).grid(column=1, row=5)
    ttk.Label(frm, text=fourStat[2]).grid(column=2, row=5)
    root.mainloop()