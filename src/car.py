import random


class Car:
    def __init__(self, car_icon):
        self.car_icon = car_icon

    @staticmethod
    def get_speed():
        car_speed = random.randint(1, 2)
        return car_speed