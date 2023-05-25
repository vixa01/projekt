import tkinter as tk

class Aplikacja:
    def __init__(self, okno):
        self.tekst = tk.StringVar()

        self.labelf = tk.Label(okno, text="FORMULARZ",bg="mediumorchid2",fg="black",font="none 16 bold")     
        self.labelf.grid(row=0,column=0,sticky="ns")

        self.labeln = tk.Label(okno, text="Imię:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labeln.grid(row=40,column=0,sticky="w")

        self.labelna = tk.Label(okno, text="Nazwisko:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelna.grid(row=41,column=0,sticky="w")

        entryn = tk.Entry(okno)
        entryn.grid(row=40, column=1)

        entryna = tk.Entry(okno)
        entryna.grid(row=41, column=1)

        self.labelwi = tk.Label(okno, text="Wiek:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelwi.grid(row=42,column=0,sticky="w")

        spin = tk.Spinbox(okno, from_= 15, to = 35)
        spin.grid(row= 42, column=1,sticky="w")

        self.labelp = tk.Label(okno, text="Płeć:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelp.grid(row=43,column=0,sticky="w")

        def radioClicked():
            print(radioValue.gt())


        radioValue = tk.IntVar()
        radio1 = tk.Radiobutton(okno, text="chłopaka", variable=radioValue, value=1, command=radioClicked,bg="mediumorchid2")
        radio1.grid(row=44,column=0,sticky="w")

        radio2 = tk.Radiobutton(okno, text="dziewczyna", variable=radioValue, value=2, command=radioClicked,bg="mediumorchid2")
        radio2.grid(row=45,column=0,sticky="w")

        radio3 = tk.Radiobutton(okno, text="nie chce podawac", variable=radioValue, value=3, command=radioClicked,bg="mediumorchid2")
        radio3.grid(row=46,column=0,sticky="w")


        self.labelo = tk.Label(okno, text="Opis:",bg="mediumorchid2", fg="black", font="none 12 bold" )
        self.labelo.grid(row=47,column=0,sticky="w")

        scrollbar = tk.Scrollbar(okno)
        textBox = tk.Text(okno,
                          height=5,
                          width=20,
                          padx=10,
                          pady=10,
                          font="Times 12 bold italic")
        
        scrollbar.grid(row=48, column=1,sticky="nsw")
        textBox.grid(row=48,column=0)
        scrollbar.config(command=textBox.yview)
        textBox.config(yscrollcommand = scrollbar.set)

        
        print("Data from text:", textBox.get(1.0,"end"))

        self.b1 =tk.Button(okno, text="wyślij",bg="white")
        self.b1.grid(row=50,column=9)

        self.b2 =tk.Button(okno, text="usuń",bg="white")
        self.b2.grid(row=50,column=10)



okno = tk.Tk()
okno.geometry("500x500")
okno.title('FORMULARZ')
okno.configure(bg='mediumorchid2')
app = Aplikacja(okno)
okno.mainloop()