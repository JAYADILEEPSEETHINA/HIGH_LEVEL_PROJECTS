import turtle

class Score:
    def __init__(self):
        self.user_score=0
        self.score_borard=turtle.Turtle()
        self.score_borard.color("white")
        self.score_borard.pencolor("white")
        self.score_borard.penup()
        self.score_borard.goto(-45, 280)
        self.score_borard.pendown()
        self.score_borard.write("SCORE : 0", False,font=('Arial', 20, 'normal'))


        self.score_borard.penup()
        self.score_borard.hideturtle()


    def add_score(self):
        self.user_score+=1
        str=f"SCORE : {self.user_score}"
        self.score_borard.clear()
        self.score_borard.write(str, False,font=('Arial', 20, 'normal'))
    def out_draw(self):
        self.out=turtle.Turtle()
        self.out.color("red")
        self.out.write(" OUT ", False, align="center",font=('Arial', 50, 'normal'))
        self.out.hideturtle()

