import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Hangman')

turtle_canvas = Canvas(master=root, width=300, height=300)
turtle_canvas.config(bg='red')
turtle_canvas.pack()

canvas = Canvas(master=root)
canvas.pack()

button_names = ['A_button', 'B_button', 'C_button', 'D_button', 'E_button', 'F_button', 'G_button', 'H_button', 'I_button', 'J_button', 'K_button', 'L_button', 'M_button'
, 'N_button', 'O_button', 'P_button', 'Q_button', 'R_button', 'S_button', 'T_button', 'U_button', 'V_button', 'W_button', 'X_button', 'Y_button', 'Z_button', 'Return', 'Close']

def print_letter(letter):
    print(letter)

create_normal_button = lambda letter: Button(canvas, text=letter, height=3, width=7, command= lambda: print_letter(letter))
create_rare_button = lambda letter: Button(canvas, text=letter, height=3, width=16, command= lambda: print_letter(letter))

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


root.mainloop()