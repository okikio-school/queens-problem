# Data Structures - N-Qs assignment


def PrintBoard(solutions):
    n = len(solutions[0])
    result = ""
    for board in solutions:
        for queen in board:
            for col in range(n):
                if col == queen:
                    result += "Q"
                else:
                    result += "-"
            result += "\n"
        result += "\n"
    print(result)
    print("For a(n) " + str(n) + "x" + str(n) +
          " chessboard we get " + str(len(solutions)) + " solutions")

# queens 8 problem


def QueensRecursive(n):
    # Array of all valid queens positions
    solutions = []

    # The index of queens array represents the row, while the value represents the column  (STACK)
    # e.g. queensArr[row] = col
    queensArr = []  

    def PlaceQueen(row, queensArr):
        # If row is n, it has successfully iterated through each row and thus has created a valid solution
        if row == n:
            solutions.append(queensArr.copy())
        else:
            # Iterate through each column in an n by n chessboard
            for col in range(n):
                # If is a valid position to place queen
                if isValidPosition(row, col, queensArr):
                    # Add valid position to array of queen positions
                    queensArr.append(col)

                    # Recursively place queens until a solution where row reaches n
                    # or until no possible solutions are found from current board placement
                    PlaceQueen(row + 1, queensArr)

                    # Backtrack regardless of whether a solution is valid or not, in order to find new solutions
                    # This is because once a solution is valid, it is pushed to the solutions array
                    queensArr.pop()
                    # Continue iterating through columns

    # Checks if the row and col given are valid spots to place a queen
    def isValidPosition(curr_col, queensArr):
        curr_row = len(queensArr)
        # Iterate through each previous queen to validate that the position for the new queen doesn't intersect
        for i in range(curr_row):
            # If column is in the same vertical path as other queens then this position isn't valid
            if queensArr[i] == curr_col:
                return False

            # Change in X
            diff_x = queensArr[i] - curr_col

            # Change in Y
            diff_y = i - curr_row

            # Slope of a pure diagonal line ("/" or "\") is 1 or -1.
            # Using slope formula `m = Δy / Δx = (y2 - y1) / (x2 - x1)`,
            # we can determine the slope of the line between our queen and previous queens based on column and row position,
            # thus to find whether the queen intersects diagonally with previous queens and if so the row and column specified aren't valid
            if abs(diff_y / diff_x) == 1:
                return False

        return True

    PlaceQueen(0, queensArr) #Run recursive method

    return solutions

    def QueensIterative():
        print()

PrintBoard(QueensRecursive(8))
PrintBoard(QueensRecursive(9))
