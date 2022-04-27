from logging import root
from tkinter import *
from tkinter import filedialog

from matplotlib.pyplot import fill
import graph
import scrap


class Application:
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root =Tk()
        self.root.title('Code des couleurs')
        Label(self.root,
              text ="Select a file on your computer or download\n the latest version of the official dataset"
              ).grid(row =1, column=1, columnspan= 2, sticky=W+E)
        Button(self.root, text ='Download',command=self.download).grid(row =2, column=1, sticky=W+E)
        Button(self.root, text ='Select',
                command =self.browseFiles).grid(row =2, column=2, sticky=W+E)
        self.root.mainloop()

    def browseFiles(self): 
        self.filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File", filetypes = (("Text files", "*.txt*"),
            ("all files", "*.*")))
        return self.filename

    def download(self):
        self.region = ["Guadeloupe",
                "Martinique",
                "Guyane",
                "La Réunion",
                "Ile-de-France",
                "Centre-Val de Loire",
                "Bourgogne-Franche-Comté",
                "Normandie",
                "Hauts-de-France",
                "Grand Est",
                "Pays de la Loire",
                "Bretagne",
                "Nouvelle-Aquitaine",
                "Occitanie",
                "Auvergne-Rhône-Alpes",
                "Provence-Alpes-Côte d’Azur",
                "Corse",
                "Saint-Pierre-et-Miquelon",
                "Mayotte",
                "Saint-Barthélemy",
                "Saint-Martin"]
    
        self.win = Toplevel(self.root)
        self.win.title("Select region")
        self.win.geometry("200x200")
        
        self.label = Label(self.win, text="select your region")
        self.label.pack()

        self.option_var = StringVar(self.win)
        self.opt = OptionMenu(self.win, self.option_var, self.region[4], *self.region, command= self.conv) #, command=graph.start(self.option_var.get())
        self.opt.pack(fill=BOTH)
        self.win.mainloop()

    def conv(self, *args):
        self.num_reg = {"Guadeloupe": "01",
                "Martinique": "02",
                "Guyane": "03",
                "La Réunion": "04",
                "Ile-de-France": "11",
                "Centre-Val de Loire": "24",
                "Bourgogne-Franche-Comté": "27",
                "Normandie": "28",
                "Hauts-de-France": "32",
                "Grand Est": "44",
                "Pays de la Loire": "52",
                "Bretagne": "53",
                "Nouvelle-Aquitaine": "75",
                "Occitanie": "76",
                "Auvergne-Rhône-Alpes": "84",
                "Provence-Alpes-Côte d’Azur": "93",
                "Corse": "94",
                "Saint-Pierre-et-Miquelon": "05",
                "Mayotte": "06",
                "Saint-Barthélemy": "07",
                "Saint-Martin": "08"}
        scrap.csv_download
        self.root.destroy()
        graph.start(self.num_reg[self.option_var.get()])
        

f = Application() 
