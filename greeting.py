#!/usr/bin/env python3
"""A simple greeting script that takes user input and provides a greeting."""

import time


def main():
    """Prompt for a name and print a greeting."""
    # Get the user's name
    name = input("Please enter your name: ")

    # Start timing
    start_time = time.perf_counter()

    # Print a personalized greeting
    print(f"\nHello, {name}! Nice to meet you!")

    # End timing and print execution time
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")


if __name__ == "__main__":
    main()
