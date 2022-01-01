#imports
import turtle as trtl
import random as rnd
import time
import stickman as s


#initialization
t = trtl.Turtle()
wn = trtl.Screen()
t.speed(0)
wn.setup(540, 960)
wn.bgpic('canvas.png')
font_setup = "Arial", 50, "bold"
t.hideturtle()

stickmanwidth = 540
stickmanheight = 960

global mistake_counter
mistake_counter = 0

#dictionary and get random word
dictionary = ['wish', 'dry', 'axiomatic', 'spell', 'believe', 'ink', 'clean', 'cheese', 'hill', 'threatening', 'behave', 'simplistic']
global word
word = dictionary[rnd.randint(0, len(dictionary) - 1)]
word = list(word)
print(word)


def write_lines():
    #Finds number of lines needed to draw.
    global number_of_lines
    number_of_lines = len(word)
    length = 540 - 10*(number_of_lines + 1)
    length = length/number_of_lines

    #Go to left-most location to start drawing lines.
    t.penup()
    t.goto(-520/2, -50)
    t.pendown()

    global list_xcor
    list_xcor = []

    for i in range(number_of_lines):
        t.penup()
        t.fd(10)
        t.pendown()
        #Add starting location of each line to list.
        xcor = t.xcor()//1
        print(xcor)
        list_xcor.append(xcor)
        t.fd(length)


def write_word(list, index):
    t.penup()
    t.goto(list[index], -50)
    t.pendown()
    t.write(word[index].upper(), font=font_setup)


def check_letter(letter):
    global mistake_counter
    exist = False
    for char in word:
        if letter == char:
            exist = True
            char_index = word.index(char)
            print(word)
            write_word(list_xcor, char_index)
            word[char_index] = '?'
    if exist == False:
        mistake_counter += 1
        if mistake_counter == 1:
            s.face(440, 540, 0, 240)
        elif mistake_counter == 2:
            s.body(440, 540, 0, 240)
        elif mistake_counter == 3:
            s.hands(440, 540, 0, 240)
        elif mistake_counter == 4:
            s.legs(440, 540, 0, 240)
        elif mistake_counter == 5:
            s.eyes(440, 540, 0, 240)
        elif mistake_counter == 6:
            s.nose(440, 540, 0, 240)
        elif mistake_counter == 7:
            s.mouth(440, 540, 0, 240)
    
    if mistake_counter >= 7:
        wn.clearscreen()
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.write('You Lost!', font=font_setup)


def end_game():
    count = 0
    for char in word:
        if char == '?':
            count += 1
    if count == len(word):
        time.sleep(1)
        wn.clearscreen()
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.write('You Won!', font=font_setup)


def gameplay(x, y):
    
    if -150 > y > -207.5:
        if -180 < x < -120:
            letter = 'a'
        elif -105 < x < -65:
            letter = 'b'
        elif -50 < x < 10:
            letter = 'c'
        elif 25 < x < 85:
            letter = 'd'
        elif 100 < x < 160:
            letter = 'e'
        
    if -217.5 > y > -275:
        if  -255 < x < -195:
            letter = 'f'
        elif -180 < x < -120:
            letter = 'g'
        elif -105 < x < -65:
            letter = 'h'
        elif -50 < x < 10:
            letter = 'i'
        elif 25 < x < 85:
            letter = 'j'
        elif 100 < x < 160:
            letter = 'k'
        elif 175 < x < 235:
            letter = 'l'

    if -285 > y > -342.5:
        if  -255 < x < -195:
            letter = 'm'
        elif -180 < x < -120:
            letter = 'n'
        elif -105 < x < -65:
            letter = 'o'
        elif -50 < x < 10:
            letter = 'p'
        elif 25 < x < 85:
            letter = 'q'
        elif 100 < x < 160:
            letter = 'r'
        elif 175 < x < 235:
            letter = 's'

    if -352.5 > y > -410:
        if  -255 < x < -195:
            letter = 't'
        elif -180 < x < -120:
            letter = 'u'
        elif -105 < x < -65:
            letter = 'v'
        elif -50 < x < 10:
            letter = 'w'
        elif 25 < x < 85:
            letter = 'x'
        elif 100 < x < 160:
            letter = 'y'
        elif 175 < x < 235:
            letter = 'z'

    try:
        check_letter(letter)
    except UnboundLocalError:
        print('')

    end_game()


write_lines()
wn.onclick(gameplay)

print('''
Hello and welcome to hangman. A word will soon be chosen randomly.
A screen with all the letters will pop-up, and make sure to click 
on letters to guess, Good luck! 
''')

wn.mainloop()




