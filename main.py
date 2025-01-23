import argparse
import tkinter as tk
from maze import Maze
from solver import MazeSolver

def main():
    parser = argparse.ArgumentParser(description="Maze Generator and Solver")
    parser.add_argument("--width", type=int, default=10, help="Width of the maze")
    parser.add_argument("--height", type=int, default=5, help="Height of the maze")
    parser.add_argument("--algo", choices=["dfs", "prim"], default="dfs",
                        help="Algorithm for generating maze")
    args = parser.parse_args()

    # Build the Maze
    maze = Maze(args.width, args.height)
    maze.build_maze(args.algo)

    # Solve the Maze
    solver = MazeSolver(maze)
    path = solver.solve_maze_bfs()

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Maze")

    # Canvas size
    cell_size = 30
    canvas_width = args.width * cell_size
    canvas_height = args.height * cell_size
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Draw the maze walls
    for y in range(args.height):
        for x in range(args.width):
            top, right, bottom, left = maze.grid[y][x]

            # Convert (y,x) to pixel coords
            # top-left corner of cell
            px_left = x * cell_size
            px_top = y * cell_size
            px_right = px_left + cell_size
            px_bottom = px_top + cell_size

            # Draw the walls if present
            if top:
                canvas.create_line(px_left, px_top, px_right, px_top, fill="black", width=2)
            if right:
                canvas.create_line(px_right, px_top, px_right, px_bottom, fill="black", width=2)
            if bottom:
                canvas.create_line(px_left, px_bottom, px_right, px_bottom, fill="black", width=2)
            if left:
                canvas.create_line(px_left, px_top, px_left, px_bottom, fill="black", width=2)

    # Highlight the path
    for (row, col) in path:
        center_x = col * cell_size + cell_size // 2
        center_y = row * cell_size + cell_size // 2
        # Draw a small circle or dot for the path
        radius = cell_size // 6
        canvas.create_oval(center_x - radius, center_y - radius,
                           center_x + radius, center_y + radius,
                           fill="red")

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
