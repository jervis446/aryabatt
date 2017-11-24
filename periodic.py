import os
from Tkinter import *
import Tkinter as tk
import tkMessageBox

#Creates and Initiates class 'App'
class table(Tk):

     
    def __init__(self):
        Tk.__init__(self)
        

        self.title("Periodic Table of the Elements")

        self.topLabel = Label(self, text = "Click the element you would like information about.", font=20)
        self.topLabel.grid(row=0,column=0,columnspan=18)
        self.createWidgets()
    


    #Names of buttons in column 1
        label1 = [
        ('1\nH', 'Hydrogen', 'Atomic # = 1\nAtomic Weight =1.01\nState = Gas\nCategory = Alkali Metals'),
        ('3\nLi', 'Lithium', 'Atomic # = 3\nAtomic Weight = 6.94\nState = Solid\nCategory = Alkali Metals'),
        ('11\nNa', 'Sodium', 'Atomic # = 11\nAtomic Weight = 22.99\nState = Solid\nCategory = Alkali Metals'),
        ('K', 'Potassium', 'Atomic # = 19\nAtomic Weight = 39.10\nState = Solid\nCategory = Alkali Metals'),
        ('Rb', 'Rubidium', 'Atomic # = 37\nAtomic Weight = 85.47\nState = Solid\nCategory = Alkali Metals'),
        ('Cs', 'Cesium', 'Atomic # = 55\nAtomic Weight = 132.91\nState = Solid\nCategory = Alkali Metals'),
        ('Fr', 'Francium', 'Atomic # = 87\nAtomic Weight = 223.00\nState = Solid\nCategory = Alkali Metals')]
        #create all buttons with a loop
        r = 1
        c = 0
        for b in label1:
            tk.Button(self,text=b[0],width=5,height=2, bg="grey",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label2 = [
        ('Be', 'Beryllium', 'Atomic # = 4\nAtomic Weight = 9.01\nState = Solid\nCategory = Alkaline Earth Metals'),
        ('Mg', 'Magnesium', 'Atomic # = 12\nAtomic Weight = 24.31\nState = Solid\nCategory = Alkaline Earth Metals'),
        ('Ca', 'Calcium', 'Atomic # = 20\nAtomic Weight = 40.08\nState = Solid\nCategory = Alkaline Earth Metals'),
        ('Sr', 'Strontium', 'Atomic # = 38\nAtomic Weight = 87.62\nState = Solid\nCategory = Alkaline Earth Metals'),
        ('Ba', 'Barium', 'Atomic # = 56\nAtomic Weight = 137.33\nState = Solid\nCategory = Alkaline Earth Metals'),
        ('Ra', 'Radium', 'Atomic # = 88\nAtomic Weight = 226.03\nState = Solid\nCategory = Alkaline Earth Metals')]
        r = 2
        c = 1
        for b in label2:
            tk.Button(self,text=b[0],width=5,height=2, bg="light green",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label3 = [
        ('Sc', 'Scandium', 'Atomic # = 21\nAtomic Weight = 44.96\nState = Solid\nCategory = Transitional Metals'),
        ('Y', 'Yttrium', 'Atomic # = 39\nAtomic Weight = 88.91\nState = Solid\nCategory = Transitional Metals'),
        ('La   >|', 'Lanthanum', 'Atomic # = 57\nAtomic Weight = 138.91\nState = Solid\nCategory = Transitional Metals'),
        ('Ac   >|', 'Actinium', 'Atomic # = 89\nAtomic Weight = 227.03\nState = Solid\nCategory = Transitional Metals')]
        r = 4
        c = 2
        for b in label3:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label4 = [
        ('Ti', 'Titanium', 'Atomic # = 22\nAtomic Weight = 47.90\nState = Solid\nCategory = Transitional Metals'),
        ('Zr', 'Zirconium', 'Atomic # = 40\nAtomic Weight = 91.22\nState = Solid\nCategory = Transitional Metals'),
        ('Hf', 'Hanium', 'Atomic # = 72\nAtomic Weight = 178.49\nState = Solid\nCategory = Transitional Metals'),
        ('Rf', 'Rutherfordium', 'Atomic # = 104\nAtomic Weight = 261.00\nState = Synthetic\nCategory = Transitional Metals')]
        r = 4
        c = 3
        for b in label4:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 10:
                r = 1
                c += 1

        label5 = [
        ('V', 'Vanadium', 'Atomic # = 23\nAtomic Weight = 50.94\nState = Solid\nCategory = Transitional Metals'),
        ('Nb', 'Niobium', 'Atomic # = 41\nAtomic Weight = 92.91\nState = Solid\nCategory = Transitional Metals'),
        ('Ta', 'Tantalum', 'Atomic # = 73\nAtomic Weight = 180.95\nState = Solid\nCategory = Transitional Metals'),
        ('Ha', 'Hahnium', 'Atomic # = 105\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Transitional Metals')]
        r = 4
        c = 4
        for b in label5:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 10:
                r = 1
                c += 1

        label6 = [
        ('Cr', 'Chromium', 'Atomic # = 24\nAtomic Weight = 51.99\nState = Solid\nCategory = Transitional Metals'),
        ('Mo', 'Molybdenum', 'Atomic # = 42\nAtomic Weight = 95.94\nState = Solid\nCategory = Transitional Metals'),
        ('W', 'Tungsten', 'Atomic # = 74\nAtomic Weight = 183.85\nState = Solid\nCategory = Transitional Metals'),
        ('Sg', 'Seaborgium', 'Atomic # = 106\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Transitional Metals')]
        r = 4
        c = 5
        for b in label6:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label7 = [
        ('Mn', 'Manganese', 'Atomic # = 25\nAtomic Weight = 178.49\nState = Solid\nCategory = Transitional Metals'),
        ('Tc', 'Technetium', 'Atomic # = 43\nAtomic Weight = 178.49\nState = Synthetic\nCategory = Transitional Metals'),
        ('Re', 'Rhenium', 'Atomic # = 75\nAtomic Weight = 178.49\nState = Solid\nCategory = Transitional Metals'),
        ('Bh', 'Bohrium', 'Atomic # = 107\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Transitional Metals')]
        r = 4
        c = 6
        for b in label7:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label8 = [
        ('Fe', 'Iron', 'Atomic # = 26\nAtomic Weight = 55.85\nState = Solid\nCategory = Transitional Metals'),
        ('Ru', 'Ruthenium', 'Atomic # = 44\nAtomic Weight = 101.07\nState = Solid\nCategory = Transitional Metals'),
        ('Os', 'Osmium', 'Atomic # = 76\nAtomic Weight = 190.20\nState = Solid\nCategory = Transitional Metals'),
        ('Hs', 'Hassium', 'Atomic # = 108\nAtomic Weight = 265.00\nState = Synthetic\nCategory = Transitional Metals')]
        r = 4
        c = 7
        for b in label8:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label9 = [
        ('Co', 'Cobalt', 'Atomic # = 27\nAtomic Weight = 58.93\nState = Solid\nCategory = Transitional Metals'),
        ('Rh', 'Rhodium', 'Atomic # = 45\nAtomic Weight = 102.91\nState = Solid\nCategory = Transitional Metals'),
        ('Ir', 'Iridium', 'Atomic # = 77\nAtomic Weight = 192.22\nState = Solid\nCategory = Transitional Metals'),
        ('Mt', 'Meitnerium', 'Atomic # = 109\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Transitional Metals')]
        r = 4
        c = 8
        for b in label9:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label10 = [
        ('Ni', 'Nickle', 'Atomic # = 28\nAtomic Weight = 58.70\nState = Solid\nCategory = Transitional Metals'),
        ('Pd', 'Palladium', 'Atomic # = 46\nAtomic Weight = 106.40\nState = Solid\nCategory = Transitional Metals'),
        ('Pt', 'Platinum', 'Atomic # = 78\nAtomic Weight = 195.09\nState = Solid\nCategory = Transitional Metals')]
        r = 4
        c = 9
        for b in label10:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        label11 = [
        ('Cu', 'Copper', 'Atomic # = 29\nAtomic Weight = 63.55\nState = Solid\nCategory = Transitional Metals'),
        ('Ag', 'Silver', 'Atomic # = 47\nAtomic Weight = 107.97\nState = Solid\nCategory = Transitional Metals'),
        ('Au', 'Gold', 'Atomic # = 79\nAtomic Weight = 196.97\nState = Solid\nCategory = Transitional Metals')]
        r = 4
        c = 10
        for b in label11:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column12 = [
        ('Zn', 'Zinc', 'Atomic # = 30\nAtomic Weight = 65.37\nState = Solid\nCategory = Transitional Metals'),
        ('Cd', 'Cadmium', 'Atomic # = 48\nAtomic Weight = 112.41\nState = Solid\nCategory = Transitional Metals'),
        ('Hg', 'Mercury', 'Atomic # = 80\nAtomic Weight = 200.59\nState = Liquid\nCategory = Transitional Metals')]
        r = 4
        c = 11
        for b in column12:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column13_1 = [
        ('B', 'Boron', 'Atomic # = 5\nAtomic Weight = 10.81\nState = Solid\nCategory = Nonmetals')]
        r = 2
        c = 12
        for b in column13_1:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Blue",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column13_2 = [
        ('Al', 'Aluminum', 'Atomic # = 13\nAtomic Weight = 26.98\nState = Solid\nCategory = Other Metals'),
        ('Ga', 'Gallium', 'Atomic # = 31\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals'),
        ('In', 'Indium', 'Atomic # = 49\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals'),
        ('Ti', 'Thallium', 'Atomic # = 81\nAtomic Weight = 204.37\nState = Solid\nCategory = Other Metals')]
        r = 3
        c = 12
        for b in column13_2:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Pink",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column14_1 = [
        ('C', 'Carbon', 'Atomic # = 6\nAtomic Weight = 12.01\nState = Solid\nCategory = Nonmetals'),
        ('Si', 'Silicon', 'Atomic # = 14\nAtomic Weight = 28.09\nState = Solid\nCategory = Nonmetals')]
        r = 2
        c = 13
        for b in column14_1:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Blue",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column14_2 = [
        ('Ge', 'Germanium', 'Atomic # = 32\nAtomic Weight = 72.59\nState = Solid\nCategory = Other Metals'),
        ('Sn', 'Tin', 'Atomic # = 50\nAtomic Weight = 118.69\nState = Solid\nCategory = Other Metals'),
        ('Pb', 'Lead', 'Atomic # = 82\nAtomic Weight = 207.20\nState = Solid\nCategory = Other Metals')]
        r = 4
        c = 13
        for b in column14_2:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Pink",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column15_1 = [
        ('N', 'Nitrogen', 'Atomic # = 7\nAtomic Weight = 14.01\nState = Gas\nCategory = Nonmetals'),
        ('P', 'Phosphorus', 'Atomic # = 15\nAtomic Weight = 30.97\nState = Solid\nCategory = Nonmetals'),
        ('As', 'Arsenic', 'Atomic # = 33\nAtomic Weight = 74.92\nState = Solid\nCategory = Nonmetals')]
        r = 2
        c = 14
        for b in column15_1:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Blue",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column15_2 = [
        ('Sb', 'Antimony', 'Atomic # = 51\nAtomic Weight = 121.75\nState = Solid\nCategory = Other Metals'),
        ('Bi', 'Bismuth', 'Atomic # = 83\nAtomic Weight = 208.98\nState = Solid\nCategory = Other Metals')]
        r = 5
        c = 14
        for b in column15_2:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Pink",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column16_1 = [
        ('O', 'Oxygen', 'Atomic # = 8\nAtomic Weight = 15.99\nState = Gas\nCategory = Nonmetals'),
        ('S', 'Sulfur', 'Atomic # = 16\nAtomic Weight = 32.06\nState = Solid\nCategory = Nonmetals'),
        ('Se', 'Selenium', 'Atomic # = 34\nAtomic Weight = 78.96\nState = Solid\nCategory = Nonmetals'),
        ('Te', 'Tellurium', 'Atomic # = 52\nAtomic Weight = 127.60\nState = Solid\nCategory = Nonmetals')]
        r = 2
        c = 15
        for b in column16_1:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Blue",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column16_2 = [
        ('Po', 'Polonium', 'Atomic # = 84\nAtomic Weight = 209.00\nState = Solid\nCategory = Other Metals')]
        r = 6
        c = 15
        for b in column16_2:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Pink",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column17 = [
        ('F', 'Fluorine', 'Atomic # = 9\nAtomic Weight = 18.99\nState = Gas\nCategory = Nonmetals'),
        ('Cl', 'Chlorine', 'Atomic # = 17\nAtomic Weight = 35.45\nState = Gas\nCategory = Nonmetals'),
        ('Br', 'Bromine', 'Atomic # = 35\nAtomic Weight = 79.90\nState = Liquid\nCategory = Nonmetals'),
        ('I', 'Iodine', 'Atomic # = 53\nAtomic Weight = 126.90\nState = Solid\nCategory = Nonmetals'),
        ('At', 'Astatine', 'Atomic # = 85\nAtomic Weight = 210.00\nState = Solid\nCategory = Nonmetals')]
        r = 2
        c = 16
        for b in column17:
            tk.Button(self,text=b[0],width=5,height=2, bg="Light Blue",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column18 = [
        ('He', 'Helium', 'Atomic # = 2\nAtomic Weight = 4.00\nState = Gas\nCategory = Nobel Gases'),
        ('Ne', 'Neon', 'Atomic # = 10\nAtomic Weight = 20.18\nState = Gas\nCategory = Nobel Gases'),
        ('Ar', 'Argon', 'Atomic # = 18\nAtomic Weight = 39.95\nState = Gas\nCategory = Nobel Gases'),
        ('Kr', 'Krypton', 'Atomic # = 36\nAtomic Weight = 83.80\nState = Gas\nCategory = Nobel Gases'),
        ('Xe', 'Xenon', 'Atomic # = 54\nAtomic Weight = 131.30\nState = Gas\nCategory = Nobel Gases'),
        ('Rn', 'Radon', 'Atomic # = 86\nAtomic Weight = 222.00\nState = Gas\nCategory = Nobel Gases')]
        r = 1
        c = 17
        for b in column18:
            tk.Button(self,text=b[0],width=5,height=2, bg="indian red",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        self.fillerLine = Label(self, text = "")
        self.fillerLine.grid(row=10, column=0)

        lanthanide = [
        ('>| Ce', 'Cerium', 'Atomic # = 58\nAtomic Weight = 140.12\nState = Solid\nCategory = Transitional Metals'),
        ('Pr', 'Praseodymium', 'Atomic # = 59\nAtomic Weight = 140.91\nState = Solid\nCategory = Transitional Metals'),
        ('Nd', 'Neodymium', 'Atomic # = 60\nAtomic Weight = 144.24\nState = Solid\nCategory = Transitional Metals'),
        ('Pm', 'Promethium', 'Atomic # = 61\nAtomic Weight = 145.00\nState = Synthetic\nCategory = Transitional Metals'),
        ('Sm', 'Samarium', 'Atomic # = 62\nAtomic Weight = 150.40\nState = Solid\nCategory = Transitional Metals'),
        ('Eu', 'Europium', 'Atomic # = 63\nAtomic Weight = 151.96\nState = Solid\nCategory = Transitional Metals'),
        ('Gd', 'Gadolinium', 'Atomic # = 64\nAtomic Weight = 157.25\nState = Solid\nCategory = Transitional Metals'),
        ('Tb', 'Terbium', 'Atomic # = 65\nAtomic Weight = 158.93\nState = Solid\nCategory = Transitional Metals'),
        ('Dy', 'Dyprosium', 'Atomic # = 66\nAtomic Weight = 162.50\nState = Solid\nCategory = Transitional Metals'),
        ('Ho', 'Holmium', 'Atomic # = 67\nAtomic Weight = 164.93\nState = Solid\nCategory = Transitional Metals'),
        ('Er', 'Erbium', 'Atomic # = 68\nAtomic Weight = 167.26\nState = Solid\nCategory = Transitional Metals'),
        ('Tm', 'Thulium', 'Atomic # = 69\nAtomic Weight = 168.93\nState = Solid\nCategory = Transitional Metals'),
        ('Yb', 'Ytterbium', 'Atomic # = 70\nAtomic Weight = 173.04\nState = Solid\nCategory = Transitional Metals'),
        ('Lu', 'Lutetium', 'Atomic # = 71\nAtomic Weight = 174.97\nState = Solid\nCategory = Transitional Metals')]
        r = 11
        c = 3
        for b in lanthanide:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            c += 1
            if c > 18:
                c = 1
                r += 1

        Actinide = [
        ('>| Th', 'Thorium', 'Atomic # = 90\nAtomic Weight = 232.04\nState = Solid\nCategory = Transitional Metals'),
        ('Pa', 'Protactinium', 'Atomic # = 91\nAtomic Weight = 231.04\nState = Solid\nCategory = Transitional Metals'),
        ('U', 'Uranium', 'Atomic # = 92\nAtomic Weight = 238.03\nState = Solid\nCategory = Transitional Metals'),
        ('Np', 'Neptunium', 'Atomic # = 93\nAtomic Weight = 237.05\nState = Synthetic\nCategory = Transitional Metals'),
        ('Pu', 'Plutonium', 'Atomic # = 94\nAtomic Weight = 244.00\nState = Synthetic\nCategory = Transitional Metals'),
        ('Am', 'Americium', 'Atomic # = 95\nAtomic Weight = 243.00\nState = Synthetic\nCategory = Transitional Metals'),
        ('Cm', 'Curium', 'Atomic # = 96\nAtomic Weight = 247\nState = Synthetic\nCategory = Transitional Metals'),
        ('Bk', 'Berkelium', 'Atomic # = 97\nAtomic Weight = 247\nState = Synthetic\nCategory = Transitional Metals'),
        ('Cf', 'Californium', 'Atomic # = 98\nAtomic Weight = 247\nState = Synthetic\nCategory = Transitional Metals'),
        ('Es', 'Einsteinium', 'Atomic # = 99\nAtomic Weight = 252.00\nState = Synthetic\nCategory = Transitional Metals'),
        ('Fm', 'Fermium', 'Atomic # = 100\nAtomic Weight = 257.00\nState = Synthetic\nCategory = Transitional Metals'),
        ('Md', 'Mendelevium', 'Atomic # = 101\nAtomic Weight = 260.00\nState = Synthetic\nCategory = Transitional Metals'),
        ('No', 'Nobelium', 'Atomic # = 102\nAtomic Weight = 259\nState = Synthetic\nCategory = Transitional Metals'),
        ('Lr', 'Lawrencium', 'Atomic # = 103\nAtomic Weight = 262\nState = Synthetic\nCategory = Transitional Metals')]
        r = 12
        c = 3
        for b in Actinide:
            tk.Button(self,text=b[0],width=5,height=2, bg="light goldenrod",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
            c += 1
            if c > 18:
                c = 1
                r += 1

        


        self.mainloop()
    def reset(self):
            reset = [
            ('Reset', 'Click the element you would like information about.', '')]
            r = 12
            c = 0
            for b in reset:
                  tk.Button(self,text=b[0],width=5,height=2, bg="black", fg="white",command=lambda text=b:self.name(text[1]) & self.info(text[2])).grid(row=r,column=c)
                  r += 1
                  if r > 7:
                       r = 1
                       c += 1

            self.infoLine = Label(self, text = "", justify = 'left')
            self.infoLine.grid(row=1,column=3,columnspan=10,rowspan=4)
    def new_game(self):
    	'''
    	When the New Game button from the menu is clicked, the game resets the score to 0 and a new question is loaded.
    	'''
    	self.load_question()
        self.score.set(0)

    def back(self):

        
        os.system('python learn1.py') 
        tk.quit()
        #self.quit()
        


    def about(self):
    	'''
    	Load the About Info Box.
    	'''
        tkMessageBox.showinfo("About Aryabhatt!","Welcome to Aryabhatt! v0.1\n Aryabhatt is developed to explore Tkinter and then started off as a simple application.\nAryabhatt! is maintained at \nhttps://github.com/jervis/Aryabhatt/ \n\nYour contributions and suggestions are welcome. Feel free to fork and pull changes to Aryabhatt! The application is open-source and is open for development.\n\nAryabhatt is developed and maintained by Adarsh kumar. For suggestions and changes, feel free to drop an email:\n kumar[dot]adarshluv99[at]gmail[dot]com .\n\nInitial Release: Nov '17.")

    def confirm_quit(self):
    	'''
    	Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.
    	'''
    	choice = tkMessageBox.askyesno('Quit Application','Are you sure you wish to stop playing Aryabhatt! ?')
    	if choice == True:
    		self.quit()
    	elif choice == False:
    		pass
    def createWidgets(self):
    	'''
    	Function that creates all the necessary Tkinter widgets. All the widgets are specified here while creation.
    	'''

    	top = self.winfo_toplevel()
    	#Creating the menu buttons
    	self.menu = tk.Menu(self)
    	self.menubar = tk.Menu(self.menu, tearoff=0)
    	self.menubar.add_command(label="New Game", command=self.new_game)
    	self.menubar.add_command(label="About", command=self.about)
        self.menubar.add_command(label="Back", command=self.back)
    	self.menubar.add_command(label="Quit", command=self.confirm_quit)
           #self.menubar.add_command(label="Reset", command=self.reset)
        

    
       
	top.config(menu=self.menubar)

  #Replaces Label at the top with the name of whichever element button was pressed
    def name(self, text):
        self.topLabel.config(text=text)

  #Displays information on the element of whichever element button was pressed
    def info(self, text):
          self.infoLine.config(text=text)

#Creates an instance of 'table' class
def main():
  a = table()

#runs main function
if __name__ == "__main__":
  main()
