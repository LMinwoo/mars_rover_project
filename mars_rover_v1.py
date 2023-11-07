class Rover:
    four_ways = ["W", "S", "E", "N"]
    x_edge = 0
    y_edge = 0

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return f"({self.x},{self.y},{self.direction})"

    def set_edge(self, x, y):
        self.x_edge = x
        self.y_edge = y

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
        if self.x + distance > 5:
            self.x = 5
        elif self.x + distance < 0:
            self.x = 0
        else:
            self.x += distance

    def move_y(self, distance):
        if self.y + distance > 5:
            self.y = 5
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

    def action(self, txt):
        for chr in txt:
            if chr == "L":
                self.rotate(chr)
            if chr == "R":
                self.rotate(chr)
            if chr == "M":
                self.move()


if __name__ == "__main__":
    rover1_set = input("Rover1 Landing: ")
    rover1_attr = rover1_set.split()
    rover1 = Rover(int(rover1_attr[0]), int(rover1_attr[1]), rover1_attr[2])
    rover1_action = input("Rover1 Instructions: ")
    rover1.action(rover1_action)

    print(rover1)
