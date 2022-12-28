from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.snake_head = self.snakes_list[0]

    def move(self):
        for index in range(len(self.snakes_list) - 1, 0, -1):
            new_x = self.snakes_list[index - 1].xcor()
            new_y = self.snakes_list[index - 1].ycor()
            self.snakes_list[index].goto(new_x, new_y)
        self.snakes_list[0].forward(20)

    def create_snake(self):
        for _ in range(3):
            my_object = Turtle(shape="square")
            my_object.color("white")
            my_object.penup()
            self.snakes_list.append(my_object)
        start_position_x = 0.00
        for object in self.snakes_list:
            object.goto(start_position_x, 0)
            start_position_x += -20

    def extend_body(self):
        x_pos_snake_tail = self.snakes_list[-1].xcor()
        y_pos_snake_tail = self.snakes_list[-1].ycor()
        my_object = Turtle(shape="square")
        my_object.color("white")
        my_object.penup()
        my_object.goto(x_pos_snake_tail, y_pos_snake_tail)
        self.snakes_list.append(my_object)

    def reset(self):
        for snake_item in self.snakes_list:
            snake_item.goto(1000, 1000)
        self.snakes_list.clear()
        self.create_snake()
        self.snake_head = self.snakes_list[0]

    def check_distance(self, compare_object):
        if self.snake_head.distance(compare_object) <= 15:
            return True
        return False

    def body_eat_check(self):
        for object_from_list in self.snakes_list[1:]:
            if self.snake_head.distance(object_from_list) < 10:
                return True

    def border_check(self):
        all_side = (
                self.snake_head.xcor() > 280 or
                self.snake_head.xcor() < -280 or
                self.snake_head.ycor() > 280 or
                self.snake_head.ycor() < -280
                    )
        if all_side is True:
            return True
        return False

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)


