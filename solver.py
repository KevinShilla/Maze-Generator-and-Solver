from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.width = maze.width
        self.height = maze.height
        self.grid = maze.grid

    def solve_maze_bfs(self):
        """Solve the maze with BFS, returning a list of (row, col) for the path."""
        start = (0, 0)
        goal = (self.height - 1, self.width - 1)
        queue = deque([start])
        visited = set([start])
        parent = {start: None}

        # BFS
        while queue:
            y, x = queue.popleft()
            if (y, x) == goal:
                return self._reconstruct_path(parent, goal)

            # Directions: Up, Right, Down, Left
            # Check each wall. If there's no wall, we can move.
            # Up
            if not self.grid[y][x][0] and y > 0:
                ny, nx = y - 1, x
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
                    queue.append((ny, nx))
            # Right
            if not self.grid[y][x][1] and x < self.width - 1:
                ny, nx = y, x + 1
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
                    queue.append((ny, nx))
            # Down
            if not self.grid[y][x][2] and y < self.height - 1:
                ny, nx = y + 1, x
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
                    queue.append((ny, nx))
            # Left
            if not self.grid[y][x][3] and x > 0:
                ny, nx = y, x - 1
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    parent[(ny, nx)] = (y, x)
                    queue.append((ny, nx))

        return []  # No path found

    def _reconstruct_path(self, parent, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path
