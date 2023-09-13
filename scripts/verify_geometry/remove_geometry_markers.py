from kiutils.board import Board
import sys

def remove_markers(board):
    board.graphicItems = [graphicItem for graphicItem in board.graphicItems if not type(graphicItem).__name__ == 'GrCircle']

board = Board.from_file(sys.argv[1])
remove_markers(board)
board.to_file(sys.argv[1])
