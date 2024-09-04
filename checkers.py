from numpy import random


def build_board(size, size2):
    checkers_board = random.choice(["Empty", "Red", "Black"], (size, size2))
    return checkers_board


def get_count(board, color):
    return len(color)


print(f"Testing out checkers' __name__ variable. Here's what's in it: {__name__}.")

if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")
