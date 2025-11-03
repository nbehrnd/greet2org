#!/usr/bin/env python3
"""Greet/bet good bye; but document script by orgmode only."""

import argparse


# fmt: off
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="""
Greet, or bet good bye to someone.  More importantly though, document
the project by a git managed README.org file instead of a README.md in
GitHub flavored Markdown.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--name",
        help="The name to address",
        metavar="str",
        type=str,
        default="Orgmode",
    )

    parser.add_argument(
        "-g",
        "--goodbye",
        help="Instead of a hello, bet good bye",
        action="store_true"
    )

    return parser.parse_args()
# fmt: on


def main():
    """Join the functionalities"""

    args = get_args()
    clause = "Good bye" if args.goodbye else "Hello"
    print(f"{clause} {args.name}!")


if __name__ == "__main__":
    main()
