# snake_game.py
# A simple Snake game using Python's standard turtle module.
# Features:
# 1) Score display
# 2) Speed control (snake speeds up as score increases)
# 3) Arrow key control
# 4) Final score shown on game over
# 5) Detailed comments

import turtle
import time
import random

# -----------------------------
# Game configuration constants
# -----------------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20  # Movement step size, also the size of one "cell"
INITIAL_DELAY = 0.12  # Initial delay between frames (seconds)
MIN_DELAY = 0.04      # Minimum delay (fastest speed)
SPEED_UP_STEP = 0.005 # How much to speed up per food eaten

# -----------------------------
# Set up the game window
# -----------------------------
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)  # Turn off automatic animation (we will manually update)

# -----------------------------
# Score display
# -----------------------------
score = 0
score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.color("white")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, SCREEN_HEIGHT // 2 - 40)
score_writer.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

# -----------------------------
# Snake head setup
# -----------------------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# -----------------------------
# Food setup
# -----------------------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# -----------------------------
# Snake body segments list
# -----------------------------
segments = []

# -----------------------------
# Movement functions
# -----------------------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    """
    Move the snake head one step in the current direction.
    """
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + GRID_SIZE)
    elif head.direction == "down":
        head.sety(y - GRID_SIZE)
    elif head.direction == "left":
        head.setx(x - GRID_SIZE)
    elif head.direction == "right":
        head.setx(x + GRID_SIZE)

# -----------------------------
# Keyboard bindings
# -----------------------------
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# -----------------------------
# Main game loop
# -----------------------------
delay = INITIAL_DELAY
game_over = False

while not game_over:
    screen.update()
    time.sleep(delay)

    # Check collision with wall
    if (head.xcor() > SCREEN_WIDTH // 2 - GRID_SIZE or
        head.xcor() < -SCREEN_WIDTH // 2 + GRID_SIZE or
        head.ycor() > SCREEN_HEIGHT // 2 - GRID_SIZE or
        head.ycor() < -SCREEN_HEIGHT // 2 + GRID_SIZE):
        game_over = True
        break

    # Check collision with food
    if head.distance(food) < GRID_SIZE:
        # Move food to a new random position aligned to the grid
        new_x = random.randint(-SCREEN_WIDTH // 2 + GRID_SIZE, SCREEN_WIDTH // 2 - GRID_SIZE)
        new_y = random.randint(-SCREEN_HEIGHT // 2 + GRID_SIZE, SCREEN_HEIGHT // 2 - GRID_SIZE)
        # Align to grid
        new_x = (new_x // GRID_SIZE) * GRID_SIZE
        new_y = (new_y // GRID_SIZE) * GRID_SIZE
        food.goto(new_x, new_y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 1
        score_writer.clear()
        score_writer.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))

        # Speed up the game slightly
        delay = max(MIN_DELAY, delay - SPEED_UP_STEP)

    # Move the snake body in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first segment to the head's current position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Move the head
    move()

    # Check collision with self
    for segment in segments:
        if segment.distance(head) < GRID_SIZE / 2:
            game_over = True
            break

# -----------------------------
# Game over message
# -----------------------------
score_writer.goto(0, 0)
score_writer.write(f"Game Over! Final Score: {score}", align="center", font=("Courier", 20, "bold"))

# Keep the window open
screen.mainloop()
