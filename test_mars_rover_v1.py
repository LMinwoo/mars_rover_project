from mars_rover_v1 import Rover


def test_init_method():
    rover = Rover(1, 2, "N")
    assert rover.x == 1
    assert rover.y == 2
    assert rover.direction == "N"


def test_edge_case_north():
    rover = Rover(1, 2, "N")
    rover.set_edge(3, 3)
    rover.move()
    rover.move()
    rover.move()
    assert rover.y == 3


def test_edge_case_east():
    rover = Rover(1, 2, "E")
    rover.set_edge(3, 3)
    rover.move()
    rover.move()
    rover.move()
    assert rover.x == 3


def test_edge_case_west():
    rover = Rover(1, 2, "W")
    rover.set_edge(3, 3)
    rover.move()
    rover.move()
    rover.move()
    assert rover.x == 0


def test_edge_case_south():
    rover = Rover(1, 2, "S")
    rover.set_edge(3, 3)
    rover.move()
    rover.move()
    rover.move()
    assert rover.y == 0


def test_rotate_funtion():
    rover = Rover(1, 2, "S")
    rover.rotate("L")
    rover.rotate("L")
    assert rover.direction == "N"


def test_action_funtion():
    rover = Rover(1, 2, "S")
    rover.set_edge(3, 3)
    rover.action("LMLMLM")
    assert rover.x == 1
    assert rover.y == 3
    assert rover.direction == "W"


def test_action_funtion_two():
    rover = Rover(1, 2, "N")
    rover.set_edge(5, 5)
    rover.action("LMLMLMLMM")
    assert rover.x == 1
    assert rover.y == 3
    assert rover.direction == "N"


def test_action_funtion_three():
    rover = Rover(3, 3, "E")
    rover.set_edge(5, 5)
    rover.action("MMRMMRMRRM")
    assert rover.x == 5
    assert rover.y == 1
    assert rover.direction == "E"
