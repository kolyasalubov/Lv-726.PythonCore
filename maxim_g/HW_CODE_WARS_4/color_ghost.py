from random import choice


class Ghost(object):

    ghost_colors = ['white', 'yellow', 'purple', 'red']
    def __init__(self):
        self.color = choice(Ghost.ghost_colors)


for _ in range(10):
    ghost = Ghost()
    print(ghost.color)