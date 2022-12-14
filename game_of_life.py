import copy


class GameOfLife:
    def __init__(self, n_rows: int, n_columns: int, coords):
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.grid = [["."] * n_columns for _ in range(n_rows)]

        for row, column in coords:
            self.grid[row][column] = "*"

    def format_grid(self):
        return "\n".join(["".join(row) for row in self.grid])

    # find coordinates of live cells - REDUNDANT FUNCTION (SEE 4TH REQUIREMENT)
    def locate_live_cells(self):
        return [
            (i, j)
            for i in range(self.n_rows)
            for j in range(self.n_columns)
            if self.grid[i][j] == "*"
        ]

    # find neighbors of a single cell
    # NOTE: also return out of bounds indexes, is ommitted in later functions with try except
    @staticmethod
    def locate_neighbors(row: int, column: int):
        neighbors = []
        neighbors.append((row, column - 1))  # left neighbor
        neighbors.append((row, column + 1))  # right neighbor
        neighbors.append((row - 1, column))  # upper neighbor
        neighbors.append((row + 1, column))  # lower neighbor
        neighbors.append((row - 1, column - 1))  # diagonal left upper
        neighbors.append((row + 1, column - 1))  # diagonal left lower
        neighbors.append((row - 1, column + 1))  # diagonal right upper
        neighbors.append((row + 1, column + 1))  # diagonal right lower
        return neighbors  # THESE ARE POSSIBLE NEIGHBORS, SO ALSO OUT OF GRID

    def count_neighbors(self, row: int, column: int):
        neighbors = GameOfLife.locate_neighbors(row, column)
        neighbor_count = 0

        for neighbor_row, neighbor_column in neighbors:
            try:
                if self.grid[neighbor_row][neighbor_column] == "*":
                    neighbor_count += 1
            except:
                continue
        return neighbor_count

    def cycle(self):
        new_grid = copy.deepcopy(self.grid)

        for row in range(self.n_rows):
            for column in range(self.n_columns):
                neighbor_count = self.count_neighbors(row, column)

                # dying because of underpopulation
                if neighbor_count < 2 or neighbor_count > 3:
                    new_grid[row][column] = "."
                # becoming alive because of lively neighbors
                elif neighbor_count == 3:
                    new_grid[row][column] = "*"

        self.grid = new_grid

        return self

    def final_board(self, n_runs: int):
        for i in range(n_runs):
            self.cycle()
            print(self.format_grid(), "\n")

        return self
