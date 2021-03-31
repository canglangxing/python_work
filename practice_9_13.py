from random import randint

class Die:
    """docstring for ClassName"""
    def __init__(self):
        self.dice = 6

    def roll_dice(self):
        random_number = randint(1, self.dice)
        print(random_number)

dice_6 = Die()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_6.roll_dice()
dice_10 = Die()
dice_10.dice = 10
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_10.roll_dice()
dice_20 = Die()
dice_20.dice = 20
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
dice_20.roll_dice()
