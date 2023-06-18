import snake
import food
import score
snake1=snake.Snake()
food1=food.Food()
food1.get_food()
my_score=score.Score()

game_on=True
while game_on:
    snake1.forward()
    if(snake1.segment_list[0].heading()==0.0):
        snake1.my_screen.onkeypress(snake1.turn_left,"Up")
        snake1.my_screen.onkeypress(snake1.turn_right,"Down")
    elif(snake1.segment_list[0].heading()==90.0):
        snake1.my_screen.onkeypress(snake1.turn_left, "Left")
        snake1.my_screen.onkeypress(snake1.turn_right, "Right")
    elif (snake1.segment_list[0].heading() == 180.0):
        snake1.my_screen.onkeypress(snake1.turn_left, "Down")
        snake1.my_screen.onkeypress(snake1.turn_right, "Up")
    elif (snake1.segment_list[0].heading() == 270.0):
        snake1.my_screen.onkeypress(snake1.turn_left, "Right")
        snake1.my_screen.onkeypress(snake1.turn_right, "Left")



    snake1.my_screen.listen()


    if(snake1.segment_list[0].xcor()>food1.x-13 and food1.x+13>snake1.segment_list[0].xcor() ):
        if(snake1.segment_list[0].ycor()>food1.y-13 and food1.y+13>snake1.segment_list[0].ycor()):
            food1.clear_food()
            snake1.add_seg()
            my_score.add_score()
    if(snake1.is_out() or snake1.is_body_touch()):
        game_on=False
        my_score.out_draw()






snake1.my_screen.exitonclick()










