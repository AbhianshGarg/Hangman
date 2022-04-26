import random as rnd
import stickman as sm
import user_application as us

def config(canvas_w):
    global stickmanwidth
    stickmanwidth = canvas_w

def get_word():
    dictionary = ['wish', 'dry', 'axiomatic', 'spell', 'believe', 'ink', 'clean', 'cheese', 'hill', 'threatening', 'behave', 'simplistic']
    word = dictionary[rnd.randint(0, len(dictionary) - 1)]
    word = list(word)
    return word

def line_math(word):
    number_of_lines = len(word)
    length = stickmanwidth - 10*(number_of_lines + 1)
    length = length/number_of_lines
    return number_of_lines, length

def check_letter(letter, word, mistake_counter, list_xcor):
    exist = False
    letter = letter.lower()
    for char in word:
        if letter == char:
            exist = True
            char_index = word.index(char)
            us.write_word(list_xcor, char_index)
            word[char_index] = '?'
    if exist == False:
        mistake_counter += 1
        if mistake_counter == 1:
            sm.face(400, 300, 10, 40)
        elif mistake_counter == 2:
            sm.body(400, 300, 10, 40)
        elif mistake_counter == 3:
            sm.hands(400, 300, 10, 40)
        elif mistake_counter == 4:
            sm.legs(400, 300, 10, 40)
        elif mistake_counter == 5:
            sm.eyes(400, 300, 10, 40)
        elif mistake_counter == 6:
            sm.nose(400, 300, 10, 40)
        elif mistake_counter == 7:
            sm.mouth(400, 300, 10, 40)

    return mistake_counter, word, char_index


