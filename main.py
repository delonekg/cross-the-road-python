import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player object
player = Player()

# Create car manager object
car_manager = CarManager()

# Create scoreboard object
scoreboard = Scoreboard()

# Event listeners for movement controls
screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collisions with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player reached the finish line
    if player.ycor() > player.finish_line:
        player.reset_position()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
