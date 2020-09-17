import datetime
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('#CCC4AD')

year = turtle.textinput("", "년도를 입력해주세요.")
month = turtle.textinput("", "달(월)을 입력해주세요.")
day = turtle.textinput("", "날(일)을 입력해주세요.")
color_list = ["#F1E53E", "#FA645C", "#572BB6"]
color_list2 = ['#DFA0B8', '#E569A8', '#7F73A8']


# function to draw calendar date
# (p, q) is the location in which calendar is drawn
# d is the number of days in each month
# m is the days of the week (sun:0, mon:1, tue:2, wed:3, thu:4, fri:5, sat:6)
def make_day(p, q, d):
    dt = datetime.datetime(int(year), int(month), int(day))

    m = dt.weekday() + 1
    if m == 7:
        m = 0

    day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    day_hash = {1: (p, q), 2: (p + 60, q), 3: (p + 120, q), 4: (p + 180, q), 5: (p + 240, q),
                6: (p + 300, q), 7: (p + 360, q), 8: (p, q - 40), 9: (p + 60, q - 40), 10: (p + 120, q - 40),
                11: (p + 180, q - 40), 12: (p + 240, q - 40), 13: (p + 300, q - 40), 14: (p + 360, q - 40),
                15: (p, q - 80), 16: (p + 60, q - 80), 17: (p + 120, q - 80), 18: (p + 180, q - 80),
                19: (p + 240, q - 80), 20: (p + 300, q - 80), 21: (p + 360, q - 80), 22: (p, q - 120),
                23: (p + 60, q - 120), 24: (p + 120, q - 120), 25: (p + 180, q - 120), 26: (p + 240, q - 120),
                27: (p + 300, q - 120), 28: (p + 360, q - 120), 29: (p, q - 160), 30: (p + 60, q - 160),
                31: (p + 120, q - 160), 32: (p + 180, q - 160), 33: (p + 240, q - 160), 34: (p + 300, q - 160),
                35: (p + 360, q - 160), 36: (p, q - 200), 37: (p + 60, q - 200), 38: (p + 120, q - 200)}

    # draw the year
    t.up()
    t.goto(p + 160, q + 60)
    t.down()
    t.pencolor("black")
    t.write(year, font=("", 20, "bold"))

    # draw the days of the week
    for i in range(7):
        t.up()
        t.goto(p + 60 * i, q + 30)
        t.down()
        t.pencolor("black")
        t.write(day_list[i])

    # draw dates
    i = 1
    while i <= d:
        t.up()
        t.goto(day_hash[i + m])
        t.down()
        t.pencolor("black")
        t.write(i)
        i += 1

    # draw a star at the date which I input
    t.up()
    t.goto(day_hash[int(day) + m])
    t.down()
    t.pensize(2)
    t.pencolor('#FDF9DD')
    t.lt(90)
    for i in range(5):
        t.fd(20)
        t.rt(144)

        
####################### Decorating function #######################

# The function of drawing a number
def one(x, y):
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.up()
        t.goto(x - 10 * i, y + 5 * i)
        t.down()
        t.color(color_list[i])
        t.lt(45)
        t.fd(100)
        t.rt(45)
        t.fd(80)
        t.rt(90)
        t.fd(400)
        t.rt(90)
        t.fd(80)
        t.rt(90)
        t.fd(300)
        t.lt(135)
        t.fd(30)
        t.goto(x - 10 * i, y + 5 * i)

def two(x, y):
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.color(color_list[i])
        t.up()
        t.goto(x - 10 * i, y + 5 * i)
        t.down()
        t.rt(90)
        t.fd(50)
        t.rt(90)
        t.fd(200)
        t.rt(90)
        t.fd(50)
        t.rt(45)
        t.fd(180)
        t.circle(40, 222)
        t.rt(90)
        t.fd(60)
        t.rt(90)
        t.circle(-100, 222)
        t.fd(120)
        t.lt(135)
        t.fd(115)

def six_nine(x, y, a):
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(x + 10 * i, y + 5 * i)
        t.down()
        if a == 6:
            t.lt(105)
            t.circle(120, 165)
            t.fd(200)
            t.circle(120, 300)
            t.rt(120)
            t.fd(100)
            t.circle(-60, 150)
            t.lt(60)
            t.fd(65)
            t.up()
            t.goto(x - 115 + 10 * i, y - 285 + 5 * i)
            t.down()
            t.circle(60)
        elif a == 9:
            t.rt(75)
            t.circle(120, 165)
            t.fd(200)
            t.circle(120, 300)
            t.rt(120)
            t.fd(100)
            t.circle(-60, 150)
            t.lt(60)
            t.fd(65)
            t.up()
            t.goto(x + 115 + 10 * i, y + 285 + 5 * i)
            t.down()
            t.circle(60)


# The function of drawing a flower
def flower(x, y, r, color):
    for i in range(6):
        t.up()
        t.goto(x, y)
        t.down()
        t.color(color)
        t.begin_fill()
        t.lt(90)
        t.fd(30 / r)
        t.rt(90)
        t.fd(200 / r)
        t.rt(90)
        t.fd(60 / r)
        t.rt(90)
        t.fd(200 / r)
        t.rt(90)
        t.fd(30 / r)
        t.end_fill()
        t.rt(30)


# The function of drawing a dot pattern
def dot(x, y, w, h, color):
    for i in range(w):
        for j in range(h):
            t.color(color_list[color])
            t.up()
            t.goto(x + i * 40, y + j * 40)
            t.down()
            t.dot()


# The function of drawing a cuboid
def cube(x, y, l):
    for i in [1, 2, 0]:
        t.up()
        t.goto(x, y)
        t.down()
        t.pencolor(color_list2[0])
        t.fillcolor(color_list2[i])
        t.begin_fill()
        t.lt(90)
        t.fd(l)
        t.rt(120)
        t.fd(l)
        t.rt(60)
        t.fd(l)
        t.rt(120)
        t.fd(l)
        t.end_fill()
        t.lt(90)


# The function of drawing a rain pattern
def rain(x, y, l):
    t.color(color_list[0])
    t.up()
    t.home()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.rt(60)
    t.fd(l)
    t.rt(10)
    t.circle(-l / 2, 220)
    t.goto(x, y)
    t.end_fill()


############################################################

################## Drawing a calendar ######################

# January
if month == '1' and int(day) <= 31:
    one(-300, -50)
    t.up()
    t.home()
    t.goto(200, 100)
    t.down()
    t.color(color_list[0])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    for i in range(3):
        t.color(color_list[i])
        t.up()
        t.goto(-400 + 10 * i, 70)
        t.down()
        t.fd(400)
        t.lt(70)
        t.fd(200)
        t.rt(140)
        t.fd(200)
        t.rt(110)
        t.fd(50)
        t.rt(110)
        t.fd(130)
        t.rt(140)
        t.fd(130)
        t.lt(70)
        t.fd(300)
        t.up()
        t.home()
        t.down()
    t.up()
    t.home()
    t.down()
    make_day(-50, -80, 31)

# February
elif month == '2':
    day_of_dec = 28
    if ((int(year) % 4 == 0) and (int(year) % 100 != 0)) or (int(year) % 400 == 0):
        day_of_dec = 29
    if int(day) > day_of_dec:
        print('You entered the date incorrectly.')
        turtle.mainloop()

    t.up()
    t.goto(250, 100)
    t.down()
    t.color(color_list[0])
    t.begin_fill()
    t.lt(135)
    t.fd(230)
    t.circle(85, 180)
    t.fd(230)
    t.end_fill()
    dot(-400, 50, 11, 6, 2)
    dot(200, -300, 4, 6, 1)
    two(330, 30)
    t.up()
    t.home()
    t.down()
    make_day(-330, -110, day_of_dec)

# March
elif month == '3' and int(day) <= 31:
    flower(-300, -200, 1, color_list[0])
    t.setheading(20)
    flower(200, 200, 1 / 2, color_list[0])
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(-350 + 10 * i, 280 + 5 * i)
        t.down()
        t.fd(300)
        t.rt(135)
        t.fd(280)
        t.lt(135)
        t.fd(50)
        t.circle(-145, 180)
        t.fd(150)
        t.up()
        t.home()
        t.goto(-350 + 10 * i, 280 + 5 * i)
        t.down()
        t.rt(90)
        t.fd(70)
        t.lt(90)
        t.fd(140)
        t.rt(135)
        t.fd(190)
        t.lt(45)
        t.fd(70)
        t.lt(90)
        t.fd(130)
        t.circle(-70, 180)
        t.fd(132)
        t.lt(90)
        t.fd(74)
    t.up()
    t.home()
    t.down()
    make_day(-55, -68, 31)

# April
elif month == '4' and int(day) <= 30:
    t.up()
    t.goto(-150, 50)
    t.down()
    t.color(color_list[0])
    t.begin_fill()
    t.fd(500)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(500)
    t.rt(90)
    t.fd(300)
    t.end_fill()
    dot(90, 10, 8, 4, 2)
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(-200 + 10 * i, 280 + 5 * i)
        t.down()
        t.fd(80)
        t.rt(90)
        t.fd(200)
        t.lt(90)
        t.fd(80)
        t.rt(90)
        t.fd(80)
        t.rt(90)
        t.fd(80)
        t.lt(90)
        t.fd(100)
        t.rt(90)
        t.fd(80)
        t.rt(90)
        t.fd(100)
        t.lt(90)
        t.fd(100)
        t.goto(-200 + 10 * i, 280 + 5 * i)
        t.up()
        t.home()
        t.goto(-200 + 10 * i, 80 + 5 * i)
        t.down()
        t.lt(90)
        t.fd(80)
        t.goto(-220 + 10 * i, 80 + 5 * i)
        t.goto(-200 + 10 * i, 80 + 5 * i)
    t.up()
    t.home()
    t.down()
    make_day(-50, -80, 30)

# May
elif month == '5' and int(day) <= 31:
    cube(-180, -50, 100)
    cube(-180, 250, 100)
    cube(-93.5, 100, 100)
    cube(-7, 250, 100)
    cube(-353, -50, 100)
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(100 + 10 * i, 200 + 5 * i)
        t.down()
        t.rt(90)
        t.fd(240)
        t.lt(90)
        t.fd(40)
        t.circle(-50, 180)
        t.fd(40)
        t.lt(90)
        t.fd(80)
        t.lt(90)
        t.fd(100)
        t.circle(120, 180)
        t.rt(90)
        t.fd(100)
        t.rt(90)
        t.fd(100)
        t.lt(90)
        t.fd(80)
        t.lt(90)
        t.fd(200)
    t.up()
    t.home()
    t.down()
    make_day(-300, -80, 31)

# June
elif month == '6' and int(day) <= 30:
    rain(100, 400, 250)
    rain(300, 0, 250)
    rain(-100, 100, 250)
    dot(-300, -300, 3, 15, 2)
    dot(100, 100, 8, 4, 1)
    six_nine(-120, 200, 6)
    t.up()
    t.home()
    t.down()
    make_day(-50, -50, 30)

# July
elif month == '7' and int(day) <= 31:
    for i in range(5):
        t.up()
        t.home()
        t.goto(-150 + 120 * i, 50)
        t.down()
        t.color(color_list[0])
        t.begin_fill()
        t.fd(80)
        t.rt(100)
        t.fd(400)
        t.rt(80)
        t.fd(80)
        t.rt(100)
        t.fd(400)
        t.end_fill()
    dot(0, 20, 10, 5, 2)
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(-330 + 10 * i, 220 + 5 * i)
        t.down()
        t.fd(230)
        t.rt(100)
        t.fd(400)
        t.rt(80)
        t.fd(80)
        t.rt(100)
        t.fd(320)
        t.lt(100)
        t.fd(150)
        t.rt(100)
        t.fd(80)
    t.up()
    t.home()
    t.down()
    make_day(-70, -80, 31)

# August
elif month == '8' and int(day) <= 31:
    t.up()
    t.goto(-300, 300)
    t.down()
    t.color(color_list[0])
    t.begin_fill()
    t.fd(700)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(700)
    t.rt(90)
    t.fd(300)
    t.end_fill()
    dot(-350, -300, 5, 20, 1)
    dot(90, -200, 8, 4, 2)
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(-170 + 10 * i, -70 + 5 * i)
        t.down()
        t.lt(20)
        t.circle(120, 340)
        t.circle(-120, 340)
        t.up()
        t.goto(-190 + 10 * i, -10 + 5 * i)
        t.down()
        t.circle(50)
        t.up()
        t.goto(-190 + 10 * i, -245 + 5 * i)
        t.down()
        t.circle(50)
    t.up()
    t.home()
    t.down()
    make_day(-50, 210, 31)

# September
elif month == '9' and int(day) <= 30:
    def three_cube(x, y):
        cube(x, y, 100)
        cube(x + 173, y, 100)
        cube(x + 173 * 2, y, 100)


    three_cube(-22.5, 350)
    three_cube(-105, 200)
    three_cube(-22.5, 50)
    six_nine(-370, -260, 9)
    t.up()
    t.home()
    t.down()
    make_day(-48, -125, 30)

# October
elif month == '10' and int(day) <= 31:
    def round_sq(x, y):
        t.up()
        t.home()
        t.goto(x, y)
        t.down()
        t.color(color_list[0])
        t.begin_fill()
        t.rt(90)
        t.circle(50, 180)
        t.fd(200)
        t.circle(50, 180)
        t.fd(200)
        t.end_fill()


    round_sq(-290, -180)
    round_sq(-140, 10)
    round_sq(10, 200)
    one(-350, 200)
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(-180 + 10 * i, 80 + 5 * i)
        t.down()
        t.rt(90)
        t.circle(100, 180)
        t.fd(200)
        t.circle(100, 180)
        t.fd(200)
        t.up()
        t.goto(-130 + 10 * i, 80 + 5 * i)
        t.down()
        t.circle(50, 180)
        t.fd(200)
        t.circle(50, 180)
        t.fd(200)
    dot(-60, 100, 10, 4, 2)
    t.up()
    t.home()
    t.down()
    make_day(-100, -100, 31)

# November
elif month == '11' and int(day) <= 30:
    cube(-200, 150, 150)
    for i in range(3):
        t.up()
        t.home()
        t.down()
        t.pencolor(color_list[i])
        t.up()
        t.goto(-200 + 10 * i, 150 + 5 * i)
        t.down()
        t.lt(30)
        for i in range(3):
            t.fd(700)
            t.backward(700)
            t.lt(120)
    one(50, 45)
    one(170, 205)
    t.up()
    t.home()
    t.down()
    make_day(-320, -80, 30)

# December
elif month == '12' and int(day) <= 31:
    for i in range(3):
        for j in range(6):
            if j > i:
                cube(-320 + i * 173, -300 + j * 150, 50)
    one(-350, 130)
    two(20, 50)
    t.up()
    t.home()
    t.down()
    make_day(-50, -80, 31)

#######################################################
else:
    print('You entered the date incorrectly.')

t.hideturtle()
turtle.mainloop()
