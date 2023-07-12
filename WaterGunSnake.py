import random


class hand_object:
    def __init__(self, handname, beats=None):
        self._handname = handname
        self._beats = beats

    @property
    def handname(self):
        return self._handname

    @property
    def beats(self):
        return self._beats

    @beats.setter
    def beats(self, beatset):
        self._beats = beatset

    def doesitbeat(self, hand_object):
        if hand_object in self.beats:
            return True
        else:
            return False


def main():
    snake = hand_object(handname="Snake")
    water = hand_object(handname="Water")
    gun = hand_object(handname="Gun")

    snake.beats = water
    water.beats = gun
    gun.beats = snake

    options = [snake, water, gun]

    while True:
        option1 = options[random.randint(0, 2)]
        option2 = options[random.randint(0, 2)]

        if option1 == option2:
            print(f"{option1.handname} == {option2.handname} Its a draw!")
        elif option1.beats == option2:
            print(f"{option1.handname} beats {option2.handname}")
        else:
            print(f"{option1.handname} looses to {option2.handname}")


main()
