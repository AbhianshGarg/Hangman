import turtle as trtl
t = trtl.Turtle()
t.speed(0)
t.hideturtle
t.pensize(3)

global limb_directions
limb_directions = [230, 305]

def ratios(canvheight, canvwidth):
    global height, width
    height = canvheight
    width = canvheight/1.5
    if width > canvwidth:
        width = canvwidth
        height = canvwidth*1.5

def face(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    x = 0 + displacementx
    y = (height/2)*0.8 + displacementy
    radius = height*0.1
    t.setheading(180)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)

def body(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    x = 0 + displacementx
    y = (height/2)*0.4 + displacementy
    t.setheading(270)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fd(height*0.3)

def hands(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    x = 0 + displacementx
    y = (height/2)*0.4 + displacementy
    t.penup()
    t.goto(x, y)
    t.pendown()
    for char in limb_directions:
        t.setheading(char)
        t.fd(height*0.2)
        t.backward(height*0.2)

def legs(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    x = 0 + displacementx
    y = (height/2)*(-0.2) + displacementy
    t.penup()
    t.goto(x, y)
    t.pendown()
    for char in limb_directions:
        t.setheading(char)
        t.fd(height*0.2)
        t.backward(height*0.2)

def eyes(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    t.setheading(180)
    y = (height/2)*0.8 + displacementy - 1/2*height*0.1
    x = 0 + displacementx - 1/2*height*0.1
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle((1/5)*height*0.1)
    x = 0 + displacementx + 1/2*height*0.1
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle((1/5)*height*0.1)
    

def nose(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    x = 0 + displacementx
    y = (height/2)*0.8 + displacementy - (7/10)*height*0.1
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(240)
    t.fd(height*0.05)
    t.setheading(0)
    t.fd(height*0.025)

def mouth(canvheight, canvwidth, displacementx, displacementy):
    ratios(canvheight, canvwidth)
    x = 0 + displacementx - 1/2*height*0.1    
    y = (height/2)*0.8 - 5/4*height*0.1 + displacementy
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(270)
    t.circle(1/2*(height*0.1), 180)



