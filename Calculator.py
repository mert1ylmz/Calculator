import tkinter
import customtkinter

# ctk settings
customtkinter.set_appearance_mode("dark")

# app frame
app = customtkinter.CTk()
app.geometry("285x325")
app.title("Calculator")
app.resizable(False, False)


# creating functions
def clickbutton(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def clearbutton():
    global expression
    expression = ""
    input_text.set("")


def equalsbutton():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except Exception as e:
        input_text.set("Error")
        expression = ""



expression = ""

input_text = customtkinter.StringVar()

# input frame
inputFrame = customtkinter.CTkFrame(app, width=279, height=50)
inputFrame.pack(side=tkinter.TOP)

# input field inside to the input frame
inputField = customtkinter.CTkEntry(inputFrame, font=("arial", 25, "bold"), textvariable=input_text, justify="right",
                                    width=279, height=50)
inputField.grid(row=0, column=0)
inputField.pack(ipady=10)

buttonFrame = customtkinter.CTkFrame(app, width=279, height=50)
buttonFrame.pack()

# button creation with command references
clear = customtkinter.CTkButton(buttonFrame, text="Clear", width=210, height=50,
                                command=clearbutton).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = customtkinter.CTkButton(buttonFrame, text="/", width=70, height=50,
                                 command=lambda: clickbutton("/")).grid(row=0, column=3, padx=1, pady=1)

seven = customtkinter.CTkButton(buttonFrame, text="7", width=70, height=50, command=lambda: clickbutton("7")).grid(
    row=1, column=0, padx=1, pady=1)
eigth = customtkinter.CTkButton(buttonFrame, text="8", width=70, height=50, command=lambda: clickbutton("8")).grid(
    row=1, column=1, padx=1, pady=1)
nine = customtkinter.CTkButton(buttonFrame, text="9", width=70, height=50, command=lambda: clickbutton("9")).grid(row=1,
                                                                                                                  column=2,
                                                                                                                  padx=1,
                                                                                                                  pady=1)

multiply = customtkinter.CTkButton(buttonFrame, text="x", width=70, height=50, command=lambda: clickbutton("*")).grid(
    row=1, column=3, padx=1, pady=1)

six = customtkinter.CTkButton(buttonFrame, text="6", width=70, height=50, command=lambda: clickbutton("6")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=1,
                                                                                                                 pady=1)

five = customtkinter.CTkButton(buttonFrame, text="5", width=70, height=50, command=lambda: clickbutton("5")).grid(row=2,
                                                                                                                  column=1,
                                                                                                                  padx=1,
                                                                                                                  pady=1)

four = customtkinter.CTkButton(buttonFrame, text="4", width=70, height=50, command=lambda: clickbutton("4")).grid(row=2,
                                                                                                                  column=2,
                                                                                                                  padx=1,
                                                                                                                  pady=1)

substract = customtkinter.CTkButton(buttonFrame, text="-", width=70, height=50, command=lambda: clickbutton("-")).grid(
    row=2, column=3, padx=1, pady=1)

three = customtkinter.CTkButton(buttonFrame, text="3", width=70, height=50, command=lambda: clickbutton("3")).grid(
    row=3, column=0, padx=1, pady=1)

two = customtkinter.CTkButton(buttonFrame, text="2", width=70, height=50, command=lambda: clickbutton("2")).grid(row=3,
                                                                                                                 column=1,
                                                                                                                 padx=1,
                                                                                                                 pady=1)

one = customtkinter.CTkButton(buttonFrame, text="1", width=70, height=50, command=lambda: clickbutton("1")).grid(row=3,
                                                                                                                 column=2,
                                                                                                                 padx=1,
                                                                                                                 pady=1)

add = customtkinter.CTkButton(buttonFrame, text="+", width=70, height=50, command=lambda: clickbutton("+")).grid(row=3,
                                                                                                                 column=3,
                                                                                                                 padx=1,
                                                                                                                 pady=1)

zero = customtkinter.CTkButton(buttonFrame, text="0", width=140, height=50, command=lambda: clickbutton("0")).grid(
    row=4, column=0, columnspan=2, padx=1, pady=1)

dot = customtkinter.CTkButton(buttonFrame, text=".", width=70, height=50, command=lambda: clickbutton(".")).grid(row=4,
                                                                                                                 column=2,
                                                                                                                 padx=1,
                                                                                                                 pady=1)

equals = customtkinter.CTkButton(buttonFrame, text="=", width=70, height=50, command=lambda: equalsbutton()).grid(row=4,
                                                                                                                  column=3,
                                                                                                                  padx=1,
                                                                                                                  pady=1)

app.mainloop()
