import tkinter as tk

class Aplikacja:
    def __init__(self, okno):
        self.tekst = tk.StringVar()

        self.labelf = tk.Label(okno, text="FORMULARZ",bg="mediumorchid2",fg="black",font="none 16 bold")     
        self.labelf.grid(row=0,column=0)

        self.labeln = tk.Label(okno, text="Imię:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labeln.grid(row=30,column=0)

        self.labelna = tk.Label(okno, text="Nazwisko:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelna.grid(row=31,column=0)

        entryn = tk.Entry(okno)
        entryn.grid(row=30, column=1)

        entryna = tk.Entry(okno)
        entryna.grid(row=31, column=1)

        self.labelwi = tk.Label(okno, text="Wiek:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelwi.grid(row=32,column=0)

        spin = tk.Spinbox(okno, from_= 0, to = 20)
        spin.grid(row= 32, column=1)

        self.labelp = tk.Label(okno, text="Płeć:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelp.grid(row=33,column=0)


        self.b1 =tk.Button(okno, text="wyślij",bg="white")
        self.b1.grid(row=50,column=22)

        self.b2 =tk.Button(okno, text="usuń",bg="white")
        self.b2.grid(row=50,column=23)



okno = tk.Tk()
okno.geometry("500x500")
okno.title('Aplikacja')
okno.configure(bg='mediumorchid2')
app = Aplikacja(okno)
okno.mainloop()




