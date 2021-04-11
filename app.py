import os
import sys
import pyautogui
import time
import argparse
import textwrap
from rich.console import Console
from nolock import no_lock
from arg import run

console = Console()

progname = """\n
█▀█ █▀█ █▀▀ █░█ █▀▀ █▄░█ ▀█▀   █▀ █░░ █▀▀ █▀▀ █▀█   █░░ █▀█ █▀▀ █▄▀   █▀ █▀▀ █▀█ █▀▀ █▀▀ █▄░█
█▀▀ █▀▄ ██▄ ▀▄▀ ██▄ █░▀█ ░█░   ▄█ █▄▄ ██▄ ██▄ █▀▀   █▄▄ █▄█ █▄▄ █░█   ▄█ █▄▄ █▀▄ ██▄ ██▄ █░▀█
            """


def main(args):
    try:
        print(progname)
        console.print(
            "\nRunning with [bold cyan]{}[/bold cyan] key.".format(args.button)
        )
        no_lock(args.button)

    except KeyboardInterrupt:
        print("\n[Process Stopped]", flush=True)

    except Exception as ex:
        print({"main": ex})


if __name__ == "__main__":
    args = run()
    main(args)