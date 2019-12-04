# /usr/bin/env python


def tot_fuel_needed(mass):
    total_fuel = 0
    new_mass = mass
    while True:
        new_mass = (new_mass//3)-2
        total_fuel += new_mass
        if new_mass < 9:
            return total_fuel


def solution_2(file_name):
    fuel = 0
    for line in open(file_name):
        fuel += tot_fuel_needed(int(line))
    return fuel


def solution_1(file_name):
    fuel = 0
    for line in open(file_name):
        fuel += int(line)//3 - 2
    return fuel


if __name__ == "__main__":
    print(tot_fuel_needed(100756))
    print("Solution 1: ", solution_1("input.txt"))
    print("Solution 2: ", solution_2("input.txt"))
