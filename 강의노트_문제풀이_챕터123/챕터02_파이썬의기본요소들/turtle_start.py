# https:://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()

# turtle.setup(1280,960)
# turtle.screensize(400,300)
t.speed("slow")
t.shape("turtle")
t.turtlesize(2)
t.color("red")
t.pencolor("blue")
t.screen.bgcolor("aqua")

# 기본 문제
# for j in range(4):
#     for i in range(4):
#         t.forward(200)
#         t.left(90)
#     t.left(90)

# 프로그래머는 패턴을 잘 파악해야한다.
# 연습문제[1/4]
# for j in range(8):
#     for i in range(4):
#         t.forward(200)
#         t.left(90)
#     t.left(45)

# 연습문제[3/4]
# for j in range(6):
#     for i in range(3):
#         t.forward(200)
#         t.left(120)
#     t.left(60)

# 연습문제[4/4]
for j in range(12):
    for i in range(6):
        t.forward(200)
        t.left(60)
    t.left(30)


turtle.done()
