__author__ = 'kpahawa'

from tkinter import *
from Scraper import *
import csv
from tkinter import ttk

class GUI:

    def __init__(self, master):
        self.master = master
        Label(self.master, text = "Please input an anime name, as precisely as possible", bg = 'white').grid(row = 0, column = 0)
        self.animeName = StringVar()
        Entry(self.master, textvariable = self.animeName).grid(row = 0, column = 1)

        self.progressBar = ttk.Progressbar(self.master, orient = HORIZONTAL, length = 300, mode = "determinate")
        self.progressBar.grid(row = 1, column = 0, sticky = EW, columnspan = 2)


        Button(self.master, command = self.executeScript , text = "Run the Script!").grid(row = 2, column = 0, sticky = EW)
    def executeScript(self):
        scraper = Scraper()

        tempName = self.animeName.get()
        tempName = tempName.split()
        tempName.append('episode')

        animeName = ""
        for i in tempName:
            animeName = animeName + i + "-"
        permAnimeName = animeName

        self.count = 1
        a = True

        while a:
            animeName = animeName + str(self.count)
            a = scraper.getHTMLTags("dummy string", animeName)
            animeName = permAnimeName

            self.count += 1

        self.writeToCSV()
    def writeToCSV(self):
        scraper = Scraper()
        finishedUltimaList = scraper.getUltimaList()
        f = open("{}.csv".format(self.animeName.get()),'w' , newline = '')
        writer = csv.writer(f)
        for row in finishedUltimaList:
            self.progressBar.step(10)
            writer.writerow(row)
        self.progressBar.stop()
        f.close()


mainwin=Tk()
mainwin.wm_title("AnimeFanpage Web Scraper")
mainwin.configure(background = "white")

gui=GUI(mainwin)
mainwin.mainloop()

# things to do: scrape off a list of anime from a website, then go through the list and scrape the individual shows.
# scraping off the list from a website shouldnt be hard.
