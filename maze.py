import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Each cell has walls: [top, right, bottom, left]
        self.grid = [
            [[True, True, True, True] for _ in range(width)]
            for _ in range(height)
        ]

    def build_maze(self, algorithm="dfs"):
        """Build the maze with either DFS or Prim's."""
        if algorithm == "dfs":
            self._build_maze_dfs()
        elif algorithm == "prim":
            self._build_maze_prim()
        else:
            print("Unknown algorithm, using DFS by default.")
            self._build_maze_dfs()

    def _build_maze_dfs(self):
        """Generate the maze using recursive backtracking (DFS)."""
        visited = [[False]*self.width for _ in range(self.height)]
        stack = [(0, 0)]
        visited[0][0] = True

        while stack:
            y, x = stack[-1]
            neighbors = []

            # Up
            if y > 0 and not visited[y - 1][x]:
                neighbors.append(("U", (y-1, x)))
            # Right
            if x < self.width - 1 and not visited[y][x + 1]:
                neighbors.append(("R", (y, x+1)))
            # Down
            if y < self.height - 1 and not visited[y + 1][x]:
                neighbors.append(("D", (y+1, x)))
            # Left
            if x > 0 and not visited[y][x - 1]:
                neighbors.append(("L", (y, x-1)))

            if neighbors:
                direction, (ny, nx) = random.choice(neighbors)
                # Remove walls between current and next
                if direction == "U":
                    self.grid[y][x][0] = False
                    self.grid[ny][nx][2] = False
                elif direction == "R":
                    self.grid[y][x][1] = False
                    self.grid[ny][nx][3] = False
                elif direction == "D":
                    self.grid[y][x][2] = False
                    self.grid[ny][nx][0] = False
                elif direction == "L":
                    self.grid[y][x][3] = False
                    self.grid[ny][nx][1] = False

                visited[ny][nx] = True
                stack.append((ny, nx))
            else:
                stack.pop()

    def _build_maze_prim(self):
        """Generate the maze using Prim's algorithm."""
        # Start with one cell in the maze
        in_maze = set()
        in_maze.add((0, 0))
        edges = []

        def add_walls(y, x):
            # Potential edges: up, right, down, left
            if y > 0:
                edges.append((y, x, "U", (y-1, x)))
            if x < self.width - 1:
                edges.append((y, x, "R", (y, x+1)))
            if y < self.height - 1:
                edges.append((y, x, "D", (y+1, x)))
            if x > 0:
                edges.append((y, x, "L", (y, x-1)))

        add_walls(0, 0)

        while edges:
            # Pick a random edge
            y, x, direction, (ny, nx) = random.choice(edges)
            edges.remove((y, x, direction, (ny, nx)))

            # If neighbor not in maze, carve
            if (ny, nx) not in in_maze:
                # Mark neighbor as in maze
                in_maze.add((ny, nx))
                # Remove walls
                if direction == "U":
                    self.grid[y][x][0] = False
                    self.grid[ny][nx][2] = False
                elif direction == "R":
                    self.grid[y][x][1] = False
                    self.grid[ny][nx][3] = False
                elif direction == "D":
                    self.grid[y][x][2] = False
                    self.grid[ny][nx][0] = False
                elif direction == "L":
                    self.grid[y][x][3] = False
                    self.grid[ny][nx][1] = False

                # Add new walls from the neighbor
                add_walls(ny, nx)
