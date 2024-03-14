from tkinter import *
import re

def my_calculator():
    class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Python Calculator")
            master.configure(bg='#009688')  

            self.screen = Text(master, state='disabled', width=80, height=5, background="#80CBC4", foreground="#ffffff", font=("times", 16, "bold"))
            self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

            self.equation = ''

            b1 =  self.createButton(7)
            b2 = self.createButton(8)
            b3 = self.createButton(9)
            b4 = self.createButton(u"\u232B", None)
            b5 = self.createButton(4)
            b6 = self.createButton(5)
            b7 = self.createButton(6)
            b8 = self.createButton(u"\u00F7")
            b9 = self.createButton(1)
            b10 = self.createButton(2)
            b11 = self.createButton(3)
            b12 = self.createButton('*')
            b13 = self.createButton('.')
            b14 = self.createButton(0)
            b15 = self.createButton('+')
            b16 = self.createButton('-')
            b17 = self.createButton('=', None, 34)

            buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

            count = 0
            for row in range(1, 5):
                for column in range(4):
                    buttons[count].grid(row=row, column=column, padx=5, pady=5)
                    count += 1
            buttons[16].grid(row=5, column=0, columnspan=4, padx=5, pady=5)

        def createButton(self, val, write=True, width=10):
            return Button(self.master, text=val, command=lambda: self.click(val, write), width=width, background="#4CAF50", foreground="#ffffff", font=("times", 16))

        def click(self, text, write):
            if write == None:
                if text == '=' and self.equation:
                    self.equation = re.sub(u"\u00F7", '/', self.equation)
                    print(self.equation)
                    answer = str(eval(self.equation))
                    self.clear_screen()
                    self.insert_screen(answer, newline=True)
                elif text == u"\u232B":
                    self.clear_screen()
            else:
                self.insert_screen(text)

        def clear_screen(self):
            self.equation = ''
            self.screen.configure(state='normal')
            self.screen.delete('1.0', END)

        def insert_screen(self, value, newline=False):
            self.screen.configure(state='normal')
            self.screen.insert(END, value)
            self.equation += str(value)
            self.screen.configure(state='disabled')

    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()

my_calculator()
