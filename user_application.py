#imports
import turtle as trtl
import random as rnd
import tkinter as tk
from tkinter import *
import time
import stickman as sm
import program_application as bck


#initialization
root = tk.Tk()
root.title('Hangman')

turtle_canvas = Canvas(master=root, width=300, height=400)
turtle_canvas.pack()
wn = trtl.TurtleScreen(turtle_canvas)
wn.bgcolor('red')
t = trtl.RawTurtle(wn)

canvas = Canvas(master=root)
canvas.pack()

font_setup = "Arial", 26, "bold"
t.speed(0)
t.hideturtle()

stickmanwidth = 300
stickmanheight = 400

global mistake_counter
mistake_counter = 0

bck.config(stickmanwidth)
sm.config(t, wn)

#dictionary and get random word
global word
word = bck.get_word()

##################

def write_lines():
    #Finds number of lines needed to draw.
    global number_of_lines
    number_of_lines, length = bck.line_math(word)

    #Go to left-most location to start drawing lines.
    t.penup()
    t.goto(-stickmanwidth/2, -150)
    t.pendown()

    global list_xcor
    list_xcor = []

    for i in range(number_of_lines):
        t.penup()
        t.fd(10)
        t.pendown()
        #Add starting location of each line to list.
        xcor = t.xcor()//1
        list_xcor.append(xcor)
        t.fd(length)


def write_word(list, index):
    t.penup()
    t.goto(list[index], -150)
    t.pendown()
    t.write(word[index].upper(), font=font_setup)


def check_letter(letter):
    global mistake_counter
    global word
    global char_index
    letter = letter.lower()
    mistake_counter, word, char_index = bck.check_letter(letter, word, mistake_counter, list_xcor)

    if mistake_counter >= 7:
        wn.clearscreen()
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.write('You Lost!', font=font_setup)
        
    end_game()


def end_game():
    count = 0
    for char in word:
        if char == '?':
            count += 1
    if count == len(word):
        wn.clearscreen()
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.write('You Won!', font=font_setup)

print(word)

button_names = ['A_button', 'B_button', 'C_button', 'D_button', 'E_button', 'F_button', 'G_button', 'H_button', 'I_button', 'J_button', 'K_button', 'L_button', 'M_button'
, 'N_button', 'O_button', 'P_button', 'Q_button', 'R_button', 'S_button', 'T_button', 'U_button', 'V_button', 'W_button', 'X_button', 'Y_button', 'Z_button', 'Return', 'Close']

create_normal_button = lambda letter: Button(canvas, text=letter, height=3, width=7, command= lambda: check_letter(letter))
create_rare_button = lambda letter: Button(canvas, text=letter, height=3, width=16, command= lambda: check_letter(letter))

row_counter = 0
run_counter = 0
column_counter = 0
for button_name in button_names:
    guess_letter = button_name[0]
    if run_counter%6 == 0 and run_counter != 0:
        row_counter += 1
        column_counter = 0
    if button_name == 'Return' or button_name == 'Close':
        button_name = create_rare_button(button_name)
        button_name.grid(row=row_counter, column=column_counter, columnspan=2)
        column_counter += 2
    else:
        button_name = create_normal_button(guess_letter)
        button_name.grid(row=row_counter, column=column_counter)
        column_counter += 1
    run_counter += 1

write_lines()

root.mainloop()



