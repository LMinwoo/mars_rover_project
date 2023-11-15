from reading_txt import get_input


class Rover:
    four_ways = ["W", "S", "E", "N"]
    x_edge = 0
    y_edge = 0
    count = 1

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return f"Rover{Rover.count}:{self.x} {self.y} {self.direction}"

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


if __name__ == "__main__":
    # get input texts
    input_txt = get_input()

    # assign Plateau size
    print(f"Plateau: {input_txt[0]}")
    plateau_set = input_txt[0]
    plateau_attr = plateau_set.split()

    # make variable for printing result
    result = []

    for x in range(1, (len(input_txt) // 2) + 1):
        # print and assign the location where Rover landing
        print(f"Rover{Rover.count} Landing: {input_txt[2 * x - 1]}")
        rover_set = input_txt[2 * x - 1]
        rover_attr = rover_set.split()
        rover = Rover(int(rover_attr[0]), int(rover_attr[1]), rover_attr[2])
        rover.set_edge(int(plateau_attr[0]), int(plateau_attr[1]))

        # print and taking cation for the Rover
        print(f"Rover{Rover.count} Instructions: {input_txt[2 * x]}")
        rover_action = input_txt[2 * x]
        rover.take_action(rover_action)

        # put the rover status for later result
        result.append(rover.__repr__())

        # counting the number of how many Rovers now working
        Rover.count += 1

    # print the total Rovers action at the end
    for x in result:
        print(x)
