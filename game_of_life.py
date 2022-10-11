class GameOfLife:
    def __init__(self, n_rows: int, n_columns: int, coords):
        grid = []
        self.n_rows = n_rows
        self.n_columns = n_columns

        for i in range(n_rows):
            line = []
            for j in range(n_columns):
                line.append(".")
            grid.append(line)

        self.grid = grid

        for row, column in coords:
            self.grid[row][column] = "*"

    def format_grid(self):
        return "\n".join(["".join(row) for row in self.grid])

    # find coordinates of live cells - REDUNDANT FUNCTION (SEE 4TH REQUIREMENT)
    def locate_live_cells(self):
        live_coords = []
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                if self.grid[i][j] == "*":
                    live_coords.append((i, j))
        return live_coords

    # find neighbors of a single cell
    # NOTE: also return out of bounds indexes, is ommitted in later functions with try except
    @classmethod
    def locate_neighbors(cls, cell_index: list):

        neighbors = []
        row = cell_index[0]
        column = cell_index[1]

        neighbors.append((row, column - 1))  # left neighbor
        neighbors.append((row, column + 1))  # right neighbor
        neighbors.append((row - 1, column))  # upper neighbor
        neighbors.append((row + 1, column))  # lower neighbor
        neighbors.append((row - 1, column - 1))  # diagonal left upper
        neighbors.append((row + 1, column - 1))  # diagonal left lower
        neighbors.append((row - 1, column + 1))  # diagonal right upper
        neighbors.append((row + 1, column + 1))  # diagonal right lower

        return neighbors  # THESE ARE POSSIBLE NEIGHBORS, SO ALSO OUT OF GRID

    def alive_count(self, cell_index: list):
        neighbors = GameOfLife.locate_neighbors(cell_index)
        alive_count = 0

        for x, y in neighbors:
            try:
                if self.grid[x][y] == "*":
                    alive_count += 1
            except:
                continue
        return alive_count

    @classmethod
    def cycle(cls, board):
        new_grid = board

        for i in range(board.n_rows):
            for j in range(board.n_columns):
                cell = [i, j]
                alive_count = board.alive_count(cell)
                # print(cell, alive_count)

                # dying because of underpopulation
                if alive_count < 2 and new_grid.grid[i][j] == "*":
                    new_grid.grid[i][j] = "."

                # dying because of overcrowding
                if alive_count > 3 and new_grid.grid[i][j] == "*":
                    new_grid.grid[i][j] = "."

                # becoming alive because of lively neighbors
                if alive_count == 3:
                    new_grid.grid[i][j] = "*"

        # print(new_grid.format_grid())
        return new_grid

    @classmethod
    def final_board(cls, board, n_runs: int):

        output = board
        # print(output.format_grid(),"\n")

        for i in range(n_runs):
            output = GameOfLife.cycle(output)
            print(output.format_grid(), "\n")

        return output
