from race import Race
from car import *
from track import *
from output import *
import time

first_car = Car('X')
second_car = Car('O')


race = 0

while True:
    print("Start race?: Y", "Save race results: S", "Quit: Q")

    user_input = str(input())
    user_input = user_input.upper()

    if user_input == 'Q':
        break

    elif user_input == 'Y':
        race += 1
        track = Track.get_track_template()
        racing_template = Race(track, first_car.car_icon, first_car.get_speed(),
              second_car.car_icon, second_car.get_speed())

        racing = Race.race_function(racing_template)

        if racing == 'X':
            output = Output(race, 'X', 'O')
            print(output.get_output_template())

        elif racing == 'O':
            output = Output(race, 'O', 'X')
            print(output.get_output_template())

        elif racing == 'T':
            output = Output(race, ' ', ' ')
            print(output.get_output_template())

    elif user_input == 'S':
        output.score_save()
        print("score saved to file")

    else:
        print("wrong input")