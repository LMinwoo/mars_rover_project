class Rover:
    four_ways = ("W", "S", "E", "N")
    x_edge = 0
    y_edge = 0
    count = 1

    def __init__(self, x, y, direction):
        try:
            if x > Rover.x_edge or x < 0:
                raise ValueError
        except ValueError:
            print("x not in valid size.")

        try:
            if y > Rover.y_edge or y < 0:
                raise ValueError
        except ValueError:
            print("y not in valid size.")

        try:
            if direction not in Rover.four_ways:
                raise ValueError
        except ValueError:
            print("direction should be one of W,S,E,N.")

        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return f"Rover{Rover.count}:{self.x} {self.y} {self.direction}"

    def set_edge(x, y):
        Rover.x_edge = x
        Rover.y_edge = y

    def move(self):
        if self.direction == "W":
            self.move_x(-1)
        if self.direction == "S":
            self.move_y(-1)
        if self.direction == "E":
            self.move_x(1)
        if self.direction == "N":
            self.move_y(1)

    def move_x(self, distance):
        if self.x + distance > self.x_edge:
            self.x = self.x_edge
        elif self.x + distance < 0:
            self.x = 0
        else:
            self.x += distance

    def move_y(self, distance):
        if self.y + distance > self.y_edge:
            self.y = self.y_edge
        elif self.y + distance < 0:
            self.y = 0
        else:
            self.y += distance

    def rotate(self, direction):
        if direction == "L":
            for i in range(4):
                if self.direction == self.four_ways[3]:
                    self.direction = self.four_ways[0]
                    break
                if self.four_ways[i] == self.direction:
                    self.direction = self.four_ways[i + 1]
                    break
        if direction == "R":
            for i in range(4):
                if self.direction == self.four_ways[0]:
                    self.direction = self.four_ways[3]
                    break
                if self.four_ways[i] == self.direction:
                    self.direction = self.four_ways[i - 1]
                    break

    def take_action(self, txt):
        for chr in txt:
            if chr == "L":
                self.rotate(chr)
            if chr == "R":
                self.rotate(chr)
            if chr == "M":
                self.move()
