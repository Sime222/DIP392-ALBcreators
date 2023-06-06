import unittest
from unittest.mock import patch
import pygame
from board import *
from play import reset_board


class TestConnect4(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_create_board(self):
        board = create_board()
        self.assertEqual(board.shape, (ROW_COUNT, COLUMN_COUNT))
        self.assertTrue(np.all(board == 0))

    def test_drop_piece(self):
        board = create_board()
        drop_piece(board, 0, 0, 1)
        self.assertEqual(board[0][0], 1)


    def test_get_next_open_row(self):
        board = create_board()
        drop_piece(board, 0, 0, 1)
        drop_piece(board, 1, 0, 1)
        drop_piece(board, 2, 0, 2)
        self.assertEqual(get_next_open_row(board, 0), 3)
        self.assertEqual(get_next_open_row(board, 1), 0)

    def test_winning_move(self):
        board = create_board()
        drop_piece(board, 0, 0, 1)
        drop_piece(board, 0, 1, 1)
        drop_piece(board, 0, 2, 1)
        drop_piece(board, 0, 3, 1)
        self.assertTrue(winning_move(board, 1))

    def test_reset_board(self):
        board = create_board()
        drop_piece(board, 0, 0, 1)
        drop_piece(board, 1, 0, 1)
        drop_piece(board, 2, 0, 2)
        reset_board(board)
        self.assertTrue(np.all(board == 0))




@patch('builtins.input', return_value='1')  # Mocks the input function and returns '1'
def test_user_input(self, input_mock):
    # Your test code that involves user input

    if __name__ == '__main__':
        unittest.main()
