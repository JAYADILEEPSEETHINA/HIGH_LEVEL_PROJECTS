import turtle
import time


class Snake:
    def __init__(self):
        self.x = None
        self.out_axis=[()]
        self.segment_list = []
        self.x_axis = [(0, 0), (-20, 0), (-40, 0)]
        self.my_screen = turtle.Screen()
        self.my_screen.setup(width=600, height=600)
        self.my_screen.bgcolor("black")
        self.my_screen.title("snake game")
        self.my_screen.tracer(0)
        for i in range(0, 3):
            self.seg = turtle.Turtle()
            self.seg.shape("square")
            self.seg.penup()
            self.seg.color("white")

            self.seg.goto(x=self.x_axis[i][0], y=self.x_axis[i][1])
            self.segment_list.append(self.seg)


    def forward(self):
        self.my_screen.update()
        time.sleep(0.1)
        for i in range(len(self.segment_list) - 1, 0, -1):
            self.x = self.segment_list[i - 1].xcor()
            self.y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(self.x, self.y)
        self.segment_list[0].forward(20)
    def turn_left(self):
        self.my_screen.update()
        time.sleep(0.1)
        for i in range(len(self.segment_list) - 1, 0, -1):
            self.x = self.segment_list[i - 1].xcor()
            self.y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(self.x, self.y)
        self.segment_list[0].left(90)
    def add_seg(self):
        self.x=self.segment_list[len(self.segment_list) - 1].xcor()
        self.y=self.segment_list[len(self.segment_list)-1].ycor()


        self.my_screen.update()
        time.sleep(0.1)
        self.seg = turtle.Turtle()
        self.seg.shape("square")
        self.seg.penup()
        self.seg.color("white")

        self.seg.goto(x=self.x, y=self.y)
        self.segment_list.append(self.seg)

        for i in range(len(self.segment_list) - 2, 0, -1):
            self.x = self.segment_list[i - 1].xcor()
            self.y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(self.x, self.y)
        self.segment_list[0].forward(20)


    def turn_right(self):
        self.my_screen.update()
        time.sleep(0.1)
        for i in range(len(self.segment_list) - 1, 0, -1):
            self.x = self.segment_list[i - 1].xcor()
            self.y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(self.x, self.y)
        self.segment_list[0].right(90)

    def is_out(self):

        if(self.segment_list[0].xcor()>=290 or self.segment_list[0].ycor()>=290 or self.segment_list[0].xcor()<=-290 or self.segment_list[0].ycor()<=-290):
            return True
        else:
            return False
    def is_body_touch(self):

        for i in range(len(self.segment_list)-1,0,-1):
            self.head_x = self.segment_list[0].xcor()
            self.head_y = self.segment_list[0].ycor()

            if(self.segment_list[i].xcor()<=self.head_x+10 and self.segment_list[i].xcor()>=self.head_x-10 and self.segment_list[i].ycor()<=self.head_y+10 and self.segment_list[i].ycor()>=self.head_y-10):

                return True

        return False



