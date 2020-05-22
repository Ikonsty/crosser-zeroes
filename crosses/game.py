from board import Board, BeyondBoardException, MarkedException


def main():
    print("This is crosses-zeroes game")
    print("You play for 'O'")
    b = Board()

    while not b.check_status(b):
        print(str(b))
        print("User Turn:")
        while True:
            try:
                r, c = input("Give your mark position(Number contain two num near: row, col)")
                b.put((int(r), int(c)), b.USER_MARK)
                break
            except ValueError:
                print("You have to give one number where:")
                print("First num is a row number, second is a col")
                print("But you have to write it together")
            except BeyondBoardException:
                print("You can choose position from 0 to 2 for row and col")
            except IndexError:
                print("You can choose position from 0 to 2 for row and col")
            except MarkedException:
                print("This cell is already filled")

        print(str(b))
        try:
            print("Computer Turn:")
            b.make_turn()
            b.put((b.lastTurn[0], b.lastTurn[1]), b.COMPUTER_MARK)
        except AttributeError:
            pass

    if b.check_status(b) == b.USER_MARK:
        print("Congratulations! You win!")
    elif b.check_status(b) == b.COMPUTER_MARK:
        print("Sorry! You lose(")
    else:
        print("Tie")

if __name__ == "__main__":
    main()
