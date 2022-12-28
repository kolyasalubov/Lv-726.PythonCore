class Ball(object):
    def __init__(self, ball='regular'):
        self.ball_type = ball


ball_1 = Ball()
ball_2 = Ball("super ball")
print(ball_1.ball_type)
print(ball_2.ball_type)
