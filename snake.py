import turtle
import time
import random

DELAY = 0.1

score = 0
high_score = 0

# Window configuration
window = turtle.Screen()
window.title("Power Snake!!")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

# Snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()  # Leaving no trace
head.goto(0, 0)
head.direction = "stop"  # Snake will wait a direction to start mooving


# Snake's body
body = []


# Score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()  # Hide the pen
text.goto(0, 260)


# Snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def resetSnakeBody():
    # Hiding body parts
    for bodyPart in body:
        bodyPart.goto(2000, 2000)

    # cleaning body list
    body.clear()


def writeScore():
    text.clear()
    text.write(f"Score: {score}      High Score: {high_score}",
               align="center", font=("Courier", 24, "normal"))


def resetScore():
    global score
    score = 0
    writeScore()


def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"


def goLeft():
    if head.direction != "right":
        head.direction = "left"


def goRight():
    if head.direction != "left":
        head.direction = "right"


# Keyboard
window.listen()
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "Down")
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")

writeScore()

while True:
    window.update()

    # Crashing with borders
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        resetSnakeBody()
        resetScore()

    # Snake is eating
    if (head.distance(food) < 20):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        newSnakeBodyPart = turtle.Turtle()
        newSnakeBodyPart.speed(0)
        newSnakeBodyPart.shape("square")
        newSnakeBodyPart.color("grey")
        newSnakeBodyPart.penup()
        body.append(newSnakeBodyPart)

        # increasing score
        score += 10

        if score > high_score:
            high_score = score
        writeScore()

    # Moving snake's body
    totalBodyParts = len(body)
    for index in range(totalBodyParts - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    if totalBodyParts > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    # Crashing with snake's body
    for bodyPart in body:
        if bodyPart.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            resetSnakeBody()
            resetScore()

    time.sleep(DELAY)
