from tkinter import *
import random

w = Tk()
w.title('Guess a number game')
w.geometry('600x400')
w.config(bg='#065569')
w.resizable(width=False, height=False)

# game logic
ranNum = random.randint(1, 10)
chance = 4
displayResult = StringVar()

def check_guess():
    global ranNum, chance

    if chance <= 0:
        displayResult.set(f"Game over! The correct number was {ranNum}.")
        user_input.config(state='disabled')
        guess_button.config(state='disabled')
        return

    try:
        userInput = int(user_input.get())
    except:
        displayResult.set("Please enter a valid number.")
        return

    if userInput == ranNum:
        msg = f"You won! {ranNum} is the right answer!"
        user_input.config(state='disabled')
        guess_button.config(state='disabled')
    elif userInput > ranNum:
        chance -= 1
        msg = f"Too high! Think of a smaller number. Attempts left: {chance}"
        user_input.delete(0, END)
    elif userInput < ranNum:
        chance -= 1
        msg = f"Too low! Think of a bigger number. Attempts left: {chance}"
        user_input.delete(0, END)

    if chance == 0 and userInput != ranNum:
        msg = f"Game over! The correct number was {ranNum}."
        user_input.config(state='disabled')
        guess_button.config(state='disabled')

    displayResult.set(msg)

title = Label(w, text='Guess A Number Game', font=('Arial', 28), fg='#fffcbd', bg='#065569')
gameInstruction = Label(w, text='Guess the number between 1 to 10 (4 attempts)', font=('Arial', 13), fg='#fffcbd', bg='#065569')

user_input = Entry(w, font=('Arial', 12))
guess_button = Button(w, text='Guess', font=('Arial', 13), fg='#13d675', bg='black', command=check_guess)
exit_button = Button(w, text='Exit Game', font=('Arial', 14), fg='white', bg='#b82741', command=w.destroy)
outputLabel = Label(w, font=('Arial', 14), fg='#fffcbd', bg='#065569', textvariable=displayResult)

title.place(x=100, y=50)
gameInstruction.place(x=150, y=95)
user_input.place(x=180, y=150)
guess_button.place(x=378, y=147)
exit_button.place(x=300, y=300)
outputLabel.place(x=60, y=220)

w.mainloop()
