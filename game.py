#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : 2048

from tkinter import *
import random

class Game(Tk):
    def __init__(self):
        super().__init__()
        self.grille = []
        for i in range(4):
            self.grille.append([])  
            for o in range(4):
                self.grille[i].append([])
        
        self.grille_old = self.grille.copy()
        self.grille_button = []
        self.gel = 0
        self.score = 0
        self.modules = [2,2,2,4]
        self.color = {
            "2":"#FFE194",
            "4":"#FFE194",
            "16":"#FFE194",
            "32":"#FFE194",
            "64":"#FFE194",
            "128":"#FFE194",
            "256":"#FFE194",
            "512":"#FFE194",
            "1024":"#FFE194",
            "2048":"#FFE194"
        }

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        
        for i in range(4):
            self.grid_columnconfigure(i, weight=1,uniform="same_group")

        self.default_button_style = {
            "bg" : "#E7B10A", "fg": "white", "highlightthickness": 0,
            "font": ("Arial", 25, "bold")
        }
        self.default_button_grid = {"padx": 2, "pady": 2, "sticky": "nsew"}

        #Line one
        self.case_0_0 = Label(self, text="", **self.default_button_style)
        self.case_0_0.grid(column=0, row=0,**self.default_button_grid)

        self.case_0_1 = Label(self, text="", **self.default_button_style)
        self.case_0_1.grid(column=1, row=0, **self.default_button_grid)
        
        self.case_0_2 = Label(self, text="", **self.default_button_style)
        self.case_0_2.grid(column=2, row=0, **self.default_button_grid)

        self.case_0_3= Label(self, text="", **self.default_button_style)
        self.case_0_3.grid(column=3, row=0, **self.default_button_grid)

        #Line two
        self.case_1_0 = Label(self, text="", **self.default_button_style)
        self.case_1_0.grid(column=0, row=1, **self.default_button_grid)

        self.case_1_1 = Label(self, text="", **self.default_button_style)
        self.case_1_1.grid(column=1, row=1, **self.default_button_grid)
        
        self.case_1_2 = Label(self, text="", **self.default_button_style)
        self.case_1_2.grid(column=2, row=1, **self.default_button_grid)

        self.case_1_3 = Label(self, text="", **self.default_button_style)
        self.case_1_3.grid(column=3, row=1, **self.default_button_grid)

        #Line three
        self.case_2_0 = Label(self, text="", **self.default_button_style)
        self.case_2_0.grid(column=0, row=2,  **self.default_button_grid)

        self.case_2_1 = Label(self, text="", **self.default_button_style)
        self.case_2_1.grid(column=1, row=2, **self.default_button_grid)
        
        self.case_2_2 = Label(self, text="", **self.default_button_style)
        self.case_2_2.grid(column=2, row=2, **self.default_button_grid)

        self.case_2_3 = Label(self, text="", **self.default_button_style)
        self.case_2_3.grid(column=3, row=2, **self.default_button_grid)

        #Line four
        self.case_3_0 = Label(self, text="", **self.default_button_style)
        self.case_3_0.grid(column=0, row=3, **self.default_button_grid)

        self.case_3_1 = Label(self, text="", **self.default_button_style)
        self.case_3_1.grid(column=1, row=3, **self.default_button_grid)
        
        self.case_3_2 = Label(self, text="", **self.default_button_style)
        self.case_3_2.grid(column=2, row=3, **self.default_button_grid)

        self.case_3_3 = Label(self, text="", **self.default_button_style)
        self.case_3_3.grid(column=3, row=3, **self.default_button_grid)

        #Line five
        self.retry = Button(self, text="Retry",command=self.new_partie,bg="red",fg="white",highlightthickness= 0,font= ("Arial", 25, "bold"))
        self.retry.grid(column=0, row=4, **self.default_button_grid)

        self.score_affiche = Label(self, text="", **self.default_button_style)
        self.score_affiche.grid(column=1,columnspan=2, row=4, **self.default_button_grid)

        self.back = Button(self, text="QUIT",command=self.QUIT,bg="red",fg="white",highlightthickness= 0,font= ("Arial", 25, "bold"))
        self.back.grid(column=3, row=4, **self.default_button_grid)

        #Touch event
        self.bind("<Key>", self.TouchePress)
        self.configure(bg="#333333", padx=10, pady=10)
        self.geometry("400x500")
        self.title("Jeu 2048")
        self.new_partie()

    def new_partie(self) -> None:
        self.score = 0
        self.gel = 0

        self.grille = []
        for i in range(4):
            self.grille.append([])  
            for o in range(4):
                self.grille[i].append([])
        
        #2 cases at the beginning
        for i in range(2):
            self.module()
        self.afficher()

    def fin(self) -> None:
        """show the score at the end of the game"""
        self.score_affiche.config(text="End : " + (str(self.score)))
        self.gel = 1
        self.score = 0

    def module(self) -> None: 
        nbr_carre_vide = 0
        for i in range(4):
            for o in range(4):
                if not self.grille[i][o]:
                    nbr_carre_vide+= 1

        if nbr_carre_vide == 0:
            self.fin()
        else:
            #new place for the new case
            self.place = random.randint(1,nbr_carre_vide)
            
            alpha = 1
            for i in range(4):
                for o in range(4):
                    if not self.grille[i][o]:
                        if alpha == self.place:
                            self.grille[i][o] = [random.choice(self.modules)]
                        alpha +=1
            
            if nbr_carre_vide == 1:
                """for i in self.grille:
                    print(i)
                fin = True
                ancien = int
                for i in range(4):
                    ancien = self.grille[i][0]
                    for o in range(1,4):
                        if ancien == self.grille[i][o]:
                            fin == False
                        print
                        ancien = self.grille[i][o]
                    
                ancien = int
                for i in range(4):
                    ancien = self.grille[0][i]
                    for o in range(1,4):
                        if ancien == self.grille[o][i]:
                            fin = False
                        ancien = self.grille[o][i]"""
                if self.check_end:
                    self.fin()

                """if fin == True:
                    print("fin car aucune action possible")
                    self.fin()"""
   
    def deplace(self,liste) -> list:
        new_liste = []
        for i in range(4):
            if not liste[i]:
                pass
            else:
                new_liste.append(liste[i])
        comp = len(new_liste)
        while comp != 4:
            new_liste.append([])
            comp +=1
        liste = new_liste
        for i in range(0,3,1):
            if liste[i] == liste[i+1]:
                if not liste[i]:
                    pass
                else:
                    self.score += liste[i][0]*2
                    liste[i] = [liste[i][0]*2]
                if i == 2:
                    liste[i+1] = []
                if i < 2:
                    liste[i+1] = liste[i+2]
                if i == 1:
                    liste[i+2] = []
                if i == 0:
                    liste[i+2] = liste[i+3]
                    liste[3] = []
        return(liste)

    def decallage(self,nbr) -> None:
        """Move the grid"""
        for tour in range(nbr):
            new_liste = [[],[],[],[]]
            j = -1
            for o in range(3,-1,-1):
                j+=1
                for i in range(4):
                    new_liste[j].append(self.grille[i][o])
            self.grille = new_liste

    def check_end(self) -> bool:
        new_grid = self.grille.clone()
        try:
            self.up()
            if new_grid == self.grille:
                self.down()
                if new_grid == self.grille:
                    self.left()
                    if new_grid == self.grille:
                        self.right()
                        if new_grid == self.grille:
                            self.grill = new_grid
                            return False
            self.grille = new_grid
            return True
        except:
            self.grille = new_grid
            return True

    def up(self) -> None:
        if self.gel == 0:
            self.decallage(1)
            for i in range(4):
                self.grille[i] = self.deplace(self.grille[i])
            self.decallage(3)
            self.module()
        if self.gel == 0:
            self.afficher()

    def down(self) -> None:
        if self.gel == 0:
            self.decallage(3)
            for i in range(4):
                self.grille[i] = self.deplace(self.grille[i])
            self.decallage(1)
            self.module()
        if self.gel == 0:
            self.afficher()
    
    def right(self) -> None:
        if self.gel == 0:
            self.decallage(2)
            for i in range(4):
                self.grille[i] = self.deplace(self.grille[i])
            self.decallage(2)
            self.module()
        if self.gel == 0:
            self.afficher()

    def left(self) -> None:
        if self.gel == 0:
            for i in range(4):
                self.grille[i] = self.deplace(self.grille[i])
            self.module()
        if self.gel == 0:
            self.afficher()

    def afficher(self) -> None:
        #Line one
        self.case_0_0.config(text=self.grille[0][0])
        self.case_0_1.config(text=self.grille[0][1])
        self.case_0_2.config(text=self.grille[0][2])
        self.case_0_3.config(text=self.grille[0][3])
        #Line two
        self.case_1_0.config(text=self.grille[1][0])
        self.case_1_1.config(text=self.grille[1][1])
        self.case_1_2.config(text=self.grille[1][2])
        self.case_1_3.config(text=self.grille[1][3])
        #Line three
        self.case_2_0.config(text=self.grille[2][0])
        self.case_2_1.config(text=self.grille[2][1])
        self.case_2_2.config(text=self.grille[2][2])
        self.case_2_3.config(text=self.grille[2][3])
        #Line four
        self.case_3_0.config(text=self.grille[3][0])
        self.case_3_1.config(text=self.grille[3][1])
        self.case_3_2.config(text=self.grille[3][2])
        self.case_3_3.config(text=self.grille[3][3])
        #Line five
        self.score_affiche.config(text=self.score)
    
    def QUIT(self) -> None:
        self.destroy()
    
    def TouchePress(self,event) -> None:
        if event.keysym == "Up":
            self.up()
        elif event.keysym == "Down":
            self.down()
        elif event.keysym == "Left":
            self.left()
        elif event.keysym == "Right":
            self.right()
        elif event.keysym == "BackSpace":
            self.new_partie()
        elif event.keysym == "Escape":
            exit()


#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : 2048