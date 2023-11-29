from mars_rover import Rover
import pytest


def test_init_method():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "N")
    assert rover.x == 1
    assert rover.y == 2
    assert rover.direction == "N"


def test_edge_case_north():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "N")
    rover.move()
    rover.move()
    rover.move()
    assert rover.y == 3


def test_edge_case_east():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "E")
    rover.move()
    rover.move()
    rover.move()
    assert rover.x == 3


def test_edge_case_west():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "W")
    rover.move()
    rover.move()
    rover.move()
    assert rover.x == 0


def test_edge_case_south():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "S")
    rover.move()
    rover.move()
    rover.move()
    assert rover.y == 0


def test_rotate_funtion():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "S")
    rover.rotate("L")
    rover.rotate("L")
    assert rover.direction == "N"


def test_action_funtion():
    Rover.set_edge(3, 3)
    rover = Rover(1, 2, "S")
    rover.take_action("LMLMLM")
    assert rover.x == 1
    assert rover.y == 3
    assert rover.direction == "W"


def test_action_funtion_two():
    Rover.set_edge(5, 5)
    rover = Rover(1, 2, "N")
    rover.take_action("LMLMLMLMM")
    assert rover.x == 1
    assert rover.y == 3
    assert rover.direction == "N"


def test_action_funtion_three():
    Rover.set_edge(5, 5)
    rover = Rover(3, 3, "E")
    rover.take_action("MMRMMRMRRM")
    assert rover.x == 5
    assert rover.y == 1
    assert rover.direction == "E"
