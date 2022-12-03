import tkinter
from tkinter import *
# window create
window = Tk()

class Calculater:
    def __init__(self):
        # Window size box
        window.title("Basic Calculater")
        window.geometry('361x458')  # box size create
        window.configure(background="#1e2128")

        self.text_input = StringVar()
        self.expression = ""

        self.entry_box()
        self.button()
        self.label()

        window.mainloop()

    # Entry box label
    def entry_box(self):
        self.entry = Entry(window, width=17, bg='#292c33', fg='white')
        self.entry.config(font=('Ink Free', 23, 'bold'), textvariable=self.text_input)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.entry.place(x=0, y=132, height=70)

    # # label and text font size
    def label(self):
        self.label = Label(window, text='Enter the Height: ', fg='white', bg='#34373d', font=('Arial', 14))
        # self.label.grid(row=0, column=0, padx=5, pady=10)
        self.label.place(x=0, y=0, height=130, width=360)

    def click(self, num):
        self.expression = self.expression + str(num)
        print(self.expression)
        self.text_input.set(self.expression)
        self.label.config(text=self.expression)

    def clear(self):
        self.expression = ""
        self.text_input.set("")

    def equal(self):
        try:
            self.total = str(eval(self.expression))
            self.text_input.set(self.total)
            self.expression = ""
            print(self.total)
            self.label.config(text=self.total)
        except:
            self.text_input.set("error")
            self.expression = ""

    def buttons(self, text, x, y):
        button = Button(window, text=text, cursor="hand2", padx=19, pady=5)
        button.config(command=lambda: self.click(text))
        button.config(font=('Ink Free', 20, 'bold'), fg='#f8d7bf', bg='#4b4d53')
        button.config(activebackground='#5a5c63', activeforeground='#C0C0C0')
        #button.grid(row=0, column=0, sticky=E, pady=200, padx=40)
        button.place(x=x, y=y, height=48, width=60)

        buttonE = Button(window, text='=', cursor="hand2")
        buttonE.config(command=lambda: self.equal())
        buttonE.config(font=('Ink Free', 20, 'bold'), fg='#f1a872', bg='#e66100')
        buttonE.config(activebackground='#f28430', activeforeground='#f0e3da')
        buttonE.place(x=228, y=400, height=48, width=125)

        buttonC = Button(window, font='Amiri', text='Clear', cursor="hand2")
        buttonC.config(command=lambda: self.clear())
        buttonC.config(font=('Ink Free', 20, 'bold'), fg='#ffffff', bg='#34373d')
        buttonC.config(activebackground='#444850', activeforeground='#C0C0C0')
        buttonC.place(x=228, y=220, height=48, width=125)

    # Button create
    def button(self):
        self.buttons('1', 12, 340)
        self.buttons('2', 85, 340)
        self.buttons('3', 158, 340)
        self.buttons('4', 12, 280)
        self.buttons('5', 85, 280)
        self.buttons('6', 158, 280)
        self.buttons('7', 12, 220)
        self.buttons('8', 85, 220)
        self.buttons('9', 158, 220)

        self.buttons('.', 85, 400)

        self.buttons('0', 12, 400)
        self.buttons('+', 158, 400)
        self.buttons('-', 228, 280)
        self.buttons('*', 295, 280)
        self.buttons('/', 228, 340)
        self.buttons('%', 295, 340)

if __name__ == '__main__':
    Calculater()
