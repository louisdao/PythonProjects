def read_data():
    while True:
        sudoku_file = input("Please input a starting sudoku puzzle: ")


        try:
            with open(sudoku_file) as newfile:
                _data = []

                for i in range(9):
                    line = newfile.readline()
                    line = line.split(',')
                    line[-1] = line[-1].strip()
                    _data.append([])

                    for j in line:
                        if j == '':
                            _data[i].append('.')
                        else:
                            _data[i].append(j)

                newfile.close()


                return _data
        except:
            continue


def print_data(plot):
    # prints first 3 row
    print()
    for i in range(3):
        print(plot[i][0], end=" ")
        print(plot[i][1], end=" ")
        print(plot[i][2], end=" ")
        print("|", end=" ")
        print(plot[i][3], end=" ")
        print(plot[i][4], end=" ")
        print(plot[i][5], end=" ")
        print("|", end=" ")
        print(plot[i][6], end=" ")
        print(plot[i][7], end=" ")
        print(plot[i][8])
    print("------+-------+------")
    # prints middle 3 row
    for i in range(3):
        print(plot[i + 3][0], end=" ")
        print(plot[i + 3][1], end=" ")
        print(plot[i + 3][2], end=" ")
        print("|", end=" ")
        print(plot[i + 3][3], end=" ")
        print(plot[i + 3][4], end=" ")
        print(plot[i + 3][5], end=" ")
        print("|", end=" ")
        print(plot[i + 3][6], end=" ")
        print(plot[i + 3][7], end=" ")
        print(plot[i + 3][8])
    print("------+-------+------")
    # prints last 3 row
    for i in range(3):
        print(plot[i + 6][0], end=" ")
        print(plot[i + 6][1], end=" ")
        print(plot[i + 6][2], end=" ")
        print("|", end=" ")
        print(plot[i + 6][3], end=" ")
        print(plot[i + 6][4], end=" ")
        print(plot[i + 6][5], end=" ")
        print("|", end=" ")
        print(plot[i + 6][6], end=" ")
        print(plot[i + 6][7], end=" ")
        print(plot[i + 6][8])
    print()
def test_data(board):
    for i in range(9):
        test = []
        for j in range(9):
            t = board[i][j]
            if t in test:
                if t != ".":
                    print("The number is shared in the same row.")
                    return False
            else:
                # if number encountered first time enter it to test list
                test.append(t)

    for k in range(9):
        test = []
        for l in range(9):
            t = board[l][k]
            if t in test:
                if t != ".":
                    print("The number is shared in the same column.")
                    return False
            else:
                test.append(t)

    # test for each cell
    for m in range(3):
        for n in range(3):
            test = []
            for o in range(3):
                for p in range(3):
                    t = board[m * 3 + o][n * 3 + p]
                    if t in test:
                        if t != ".":
                            print("The number is shared in the same 3x3 cell.")
                            return False
                    else:
                        test.append(t)

def count_space(empty_spaces):
    # returns number of empty spaces left in sudoku
    count = 0
    for i in range(9):
        for j in range(9):
            if empty_spaces[i][j] == ".":
                count += 1

    return count

board = read_data()
print_data(board)
# game = False

if test_data(board) == False:
    print("The inputted sudoku is not valid.")
else:

    while True:
        user_input = ""
        if count_space(board) == 0:
            print("Congratulation, you have solved the sudoku!")
            break
        else:
            user_input = input("Please input the row, column and number or q to quit: ")
            if user_input == "q" or user_input == "Q":
                quit()

            else:
                usr_in = user_input.split()
                valid_number = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                try:
                    row = usr_in[0]
                    col = usr_in[1]
                    number = usr_in[2]
                    row = int(row)
                    col = int(col)
                    number = int(number)

                    if row not in valid_number:
                        print("Numbers are not within 1-9 range.")
                    elif col not in valid_number:
                        print("Numbers are not within 1-9 range.")
                    elif number not in valid_number:
                        print("Numbers are not within 1-9 range.")

                    else:

                        if board[row - 1][col - 1] == ".":

                            board[row - 1][col - 1] = str(number)
                            if test_data(board) == False:

                                board[row - 1][col - 1] = "."

                            else:
                                print_data(board)

                        else:  # print error message
                            print("The cell already has a number.")
                except ValueError:
                    print("invalid input.")
                except IndexError:
                    print("invalid input.")
