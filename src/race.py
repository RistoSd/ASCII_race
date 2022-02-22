import os

class Race:
    def __init__(
            self,
            track,
            car1,
            car1_speed,
            car2,
            car2_speed
                 ):
        self.track = track
        self.car1 = car1
        self.car1_speed = car1_speed
        self.car2 = car2
        self.car2_speed = car2_speed

    def race_function(self):
        race_track1 = self.track.copy()
        race_track2 = self.track.copy()

        race_track1.append(self.car1)
        race_track2.append(self.car2)

        print(' '.join(race_track1) + "," + ' '.join(race_track2))
       

        while True:
            index1 = race_track1.index(self.car1)
            index2 = race_track2.index(self.car2)

            race_track1.pop(index1)
            race_track2.pop(index2)

            race_track1.insert(index1, '_')
            race_track2.insert(index2, '_')

            position1 = index1 - self.car1_speed
            position2 = index1 - self.car2_speed

            if position1 < 0:
                position1 = 0
            elif position2 < 0:
                position2 = 0

            race_track1.pop(position1)
            race_track2.pop(position2)

            race_track1.insert(position1, self.car1)
            race_track2.insert(position2, self.car2)

            if position1 == 0:
                return 'X'
            elif position2 == 0:
                return 'O'
            elif position1 == 0 and position2 == 0:
                return 'T'
            else:
                print(' '.join(race_track1) + "," + ' '.join(race_track2))
                



