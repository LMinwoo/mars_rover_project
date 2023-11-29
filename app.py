import click
from reading_txt import get_input
from mars_rover import Rover
from dataclasses import dataclass


@dataclass
class Plateau:
    x: int
    y: int


@click.command()
@click.argument("txt_file")
def cli(txt_file):
    # get input texts
    input_txt = get_input(txt_file)

    # assign Plateau size
    plateau_set = input_txt[0]
    plateau_attr = plateau_set.split()
    plateau = Plateau(int(plateau_attr[0]), int(plateau_attr[1]))
    Rover.set_edge(plateau.x, plateau.y)

    # make variable for printing result
    result = []

    for x in range(1, (len(input_txt) // 2) + 1):
        # print and assign the location where Rover landing
        rover_set = input_txt[2 * x - 1]
        rover_attr = rover_set.split()
        rover = Rover(int(rover_attr[0]), int(rover_attr[1]), rover_attr[2])

        # print and taking cation for the Rover
        rover_action = input_txt[2 * x]
        rover.take_action(rover_action)

        # put the rover status for later result
        result.append(rover.__repr__())

        # counting the number of how many Rovers now working
        Rover.count += 1

    # print the total Rovers action at the end
    for x in result:
        print(x)
