import random

class Ghost(object):
    def __init__(self):
        color_list = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(color_list)

