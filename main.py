import checkers


def game():
    response = int(input("What size checkers board do you want?(Pick a size between 4 and 16):"))
    print(checkers.build_board(response, response))
    print(f"Empty Cells: {checkers.get_count(response, "Empty")}")
    print(f"Red Cells: {checkers.get_count(response, "Red")}")
    print(f"Black Cells: {checkers.get_count(response, "Black")}")


if __name__ == "__main__":
    game()
