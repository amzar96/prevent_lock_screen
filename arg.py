import os
import sys
import argparse

def run():
    myoption = argparse.ArgumentParser(
        prog="Prevent Sleep Lock Screen",
        usage="%(prog)s [options] path",
        description="List the content of a folder",
        epilog="Enjoy the program! :)",
    )
    myoption.add_argument(
        "--button",
        metavar="button",
        type=str,
        default="capslock",
        help="Enter button you want to press (default is capslock)",
    )

    args = myoption.parse_args()

    return args