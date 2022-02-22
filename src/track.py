import random


class Track:
    @staticmethod
    def get_track_template():
        template = ['_']
        length = random.randint(10, 20)
        track = template * length
        return track
