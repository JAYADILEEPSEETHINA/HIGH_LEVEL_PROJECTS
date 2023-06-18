import random
import turtle


class Food:
    def __init__(self):
        self.x = None

    def get_food(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.item = turtle.Turtle()
        self.item.shape("circle")
        self.item.color("blue")
        self.item.penup()
        self.item.goto(self.x, self.y)
    def clear_food(self):
        self.item.goto(x=1000,y=1000)
        self.get_food()
