from btree import LinkedBST
from btnode import BSTNode
import random
import copy
#Create exceptions for board

class BeyondBoardException(Exception):
    '''
    Exception if mark was put beyond the board
    '''
    pass


class MarkedException(Exception):
    '''
    Exception if cell on board is already marked
    '''
    pass

#Create Board Class

class Board:

    USER_MARK = "O"
    COMPUTER_MARK = "X"

    def __init__(self):
        """
        Create new Board for playing crosses
        Board is a 2D list with positions
        """
        self._board = [[None for i in range(3)] for j in range(3)]
        self.lastTurn = (None, None)
        self.lastMark = None


    def __getitem__( self, index):
        """
        Get item from board
        """
        return self._board[index]


    def __setitem__( self, index, value ):
        self._board[index] = value


    def __str__(self):
        """
        Return Board as a str
        """
        str_board = ""

        for ln in self._board:
            for c in ln:
                if c is None:
                    str_board += "[ ]"
                else:
                    str_board += "[" + c + "]"

            str_board += "\n"

        return str_board

    @staticmethod
    def check_status(board):
        """
        Check status on the board
        Check if someone is a winner or there is a tie
        """

        for i in range(3):
            # If there is a vertical line winner
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]

            # If there is a horisontal line winner
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return board[i][0]
        # If there is a diagonal winner
        if board[0][0] == board[1][1] == board[2][2] and board[2][2] is not None:
            return board[0][0]

        if board[2][0] == board[1][1] == board[0][2] and board[0][2] is not None:
            return board[2][0]

        # If there is a tie
        for r in board:
            for c in r:
                if c is None:
                    return None
        return "Tie"


    def build_tree(self, board):
        """
        Build binary tree for board
        """
        def process(node, C_Turn):
            '''
            Help func for building tree
            '''
            is_free = bool(max([cell is None for line in node.data for cell in line]))
            if not is_free:
                return
            # Adding left tree root as board
            while True:
                position = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
                if 0 > position[0] or position[0] > 2 or 0 > position[1] or position[0] > 2 or node.data[position[0]][position[1]] is not None:
                    continue
                else:
                    break

            if Board.check_status(node.data) is not None:
                return

            new_board = copy.deepcopy(node.data)
            if C_Turn:
                new_board[position[0]][position[1]] = Board.COMPUTER_MARK
                self.lastMark = Board.COMPUTER_MARK
                self.lastTurn = position
            else:
                Board.USER_MARK
                # self.lastMark = Board.USER_MARK
                # self.lastTurn = position

            node.left = BSTNode(new_board)

            # Adding right tree root as board
            while True:
                position = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
                if 0 > position[0] or position[0] > 2 or 0 > position[1] or position[0] > 2 or node.data[position[0]][position[1]] is not None:
                    continue
                else:
                    break

            if Board.check_status(node.data) is not None:
                return

            new_board = copy.deepcopy(node.data)
            if C_Turn:
                new_board[position[0]][position[1]] = Board.COMPUTER_MARK
                self.lastMark = Board.COMPUTER_MARK
                self.lastTurn = position
            else:
                Board.USER_MARK
                # self.lastMark = Board.USER_MARK
                # self.lastTurn = position

            node.right = BSTNode(new_board)

            C_Turn = not C_Turn

            process(node.left, C_Turn)
            process(node.right, C_Turn)

        # End of helper function
        tree = LinkedBST()
        tree.add(board)

        C_Turn = False
        if self.lastMark == Board.USER_MARK or self.lastMark is None:
            C_Turn = True
        process(tree._root, C_Turn)
        return tree


    def put(self, position, mark):
        """
        Putting mark on position
        """
        if 0 > position[0] or position[0] > 2 or 0 > position[1] or position[0] > 2:
            raise BeyondBoardException("There is no such cell")

        if self._board[position[0]][position[1]] is not None:
            raise MarkedException("This cell is already filled")

        self._board[position[0]][position[1]] = mark
        self.lastMark = mark
        self.lastTurn = position


    def make_turn(self):
        """
        Choose next turn by computer
        """
        tree = self.build_tree(self._board)

        def count(node):
            '''
            Help function for count points for winning
            '''
            if node.right is None and node.left is None:
                if Board.check_status(node.data) == Board.COMPUTER_MARK:
                    return 1
                elif Board.check_status(node.data) == Board.USER_MARK:
                    return -1
                else:
                    return 0
            return count(node.left) + count(node.right)

        count_left = count(tree._root.left)
        count_right = count(tree._root.right)

        if count_right > count_left:
            return tree._root.right.data
        else:
            return tree._root.left.data

    def is_free_cell(self):
        '''
        Checking if the cell is free
        '''
        is_free = bool(max([cell is None for line in self._board for cell in line]))
        return is_free
