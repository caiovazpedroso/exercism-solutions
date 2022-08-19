"""Does this this and that"""

def square(number):
    """
    Calculates number of grains for a given numbered square
    """

    # when the square value is not in the acceptable range
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total(filled_squares):
    """
    Calculates total of grains in the chessboard for a given number of filled squares
    """

    board = 0
    # when the square value is not in the acceptable range
    if filled_squares<1 or filled_squares>64:
        raise ValueError("square must be between 1 and 64")
    for i in range(1,filled_squares+1):
        board = board + (2**(i-1))
    return board
