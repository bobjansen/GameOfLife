import copy


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
    @staticmethod
    def locate_neighbors(cell_index: list):

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

    def cycle(self):
        new_grid = copy.deepcopy(self.grid)

        for i in range(self.n_rows):
            for j in range(self.n_columns):
                cell = [i, j]
                alive_count = self.alive_count(cell)

                # dying because of underpopulation
                if alive_count < 2 or alive_count > 3:
                    new_grid[i][j] = "."
                # becoming alive because of lively neighbors
                elif alive_count == 3:
                    new_grid[i][j] = "*"

        self.grid = new_grid

        return self

    def final_board(self, n_runs: int):
        for i in range(n_runs):
            self.cycle()
            print(self.format_grid(), "\n")

        return self
