#!/usr/bin/env python3
# Created by: Ina Tolo
# Created on: Nov. 30, 2021
# This program asks the user for the base edge and
# height of the hexagonal prism in their chosen units. It then
# calculates and displays the surface area and
# volume.
import math
import colorama
from colorama import Fore


def main():
    # get input

    print("Today we will calculate the surface area and")
    print("volume of a hexagonal prism!")
    print("")
    units = str(input("Enter the units: "))
    base_edge = float(input("Enter the base edge: "))
    height = float(input("Enter the height: "))

    # calculation process for surface area

    surface_area = (3 * math.sqrt(3))
    surface_area1 = pow(base_edge, 2)
    surface_area2 = surface_area * surface_area1
    surface_area3 = 6 * base_edge
    surface_area4 = surface_area3 * height
    sA5 = surface_area2 + surface_area4

    # calculation process for volume

    volume = (3 * math.sqrt(3)) / 2
    volume1 = pow(base_edge, 2)
    volume2 = volume1 * height
    volume3 = volume * volume2

    # output display
    print("")
    print(Fore.RED + "Surface area = {:,.2f}{}^2 ". format(sA5, units))
    print(Fore.GREEN + "Volume = {:,.2f}{}^3". format(volume3, units))


if __name__ == "__main__":
    main()
