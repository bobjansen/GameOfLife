from game_of_life import GameOfLife
import pytest

demo_grid = GameOfLife(4, 8, [[1, 4], [2, 3], [2, 4]])  # equal to example


def test_create_starter_grid():
    input = demo_grid.format_grid()
    expected = """ ........
    ....*...
    ...**...
    ........""".replace(
        " ", ""
    )
    assert input == expected


def test_locate_live_coords():
    input = demo_grid.locate_live_cells()
    expected = [(1, 4), (2, 3), (2, 4)]
    assert set(input) == set(expected)


def test_locate_neighbors():
    input = GameOfLife.locate_neighbors(1, 4)
    expected = [(0, 4), (2, 4), (1, 5), (1, 3), (0, 3), (0, 5), (2, 3), (2, 5)]
    assert set(input) == set(expected)


def test_alive_count():
    input = demo_grid.alive_count(2, 4)
    expected = 2
    assert input == expected


# Note: Test cases are hard to keep and consider after implementing all rules
def test_cycle_1():
    grid = GameOfLife(4, 8, [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]])
    expected = """ *.*.....
    *.*.....
    ........
    ........""".replace(
        " ", ""
    )
    assert grid.cycle().format_grid() == expected


def test_cycle_2():
    grid = demo_grid
    expected = """ ........
    ...**...
    ...**...
    ........""".replace(
        " ", ""
    )

    assert grid.cycle().format_grid() == expected


def test_final_board():
    grid = GameOfLife(
        4,
        8,
        [
            [0, 0],
            [1, 0],
            [2, 0],
            [3, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
        ],
    )
    expected = """ ........
    ........
    ........
    ........""".replace(
        " ", ""
    )
    assert grid.final_board(100).format_grid() == expected
