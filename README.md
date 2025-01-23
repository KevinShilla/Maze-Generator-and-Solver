# 🎮 Maze Generator and Solver

Welcome to **Maze Generator and Solver**, a Python project for generating and solving mazes with multiple algorithms and a graphical interface. This tool allows you to customize the maze size, choose generation algorithms, and visualize the solution path interactively.

---

## 🔘 Features

- **Maze Generation Algorithms:**
  - 🔄 **Depth-First Search (DFS):** Recursive backtracking.
  - ✨ **Prim's Algorithm:** Randomized spanning tree approach.
- **Maze Solving Algorithm:**
  - 🔀 **Breadth-First Search (BFS):** Finds the shortest path.
- **Graphical User Interface (GUI):**
  - Visualizes the maze structure and solution path with red dots.
- **Command-Line Options:**
  - Easily set maze dimensions and choose algorithms.

---

## 🔧 Installation

### Prerequisites

- **Python 3.7+**
- Tkinter (included with most Python distributions)

### Clone Repository

```bash
# Clone the project repository
git clone https://github.com/<KevinShilla>/maze-generator-solver.git
cd maze-generator-solver
```

---

## ⚙️ Usage

### Running the Program

```bash
python main.py --width <width> --height <height> --algo <algorithm>
```

#### Command-Line Arguments

| Argument         | Description                                   | Default Value |
|------------------|-----------------------------------------------|---------------|
| `--width`        | Width of the maze (number of columns)         | `10`          |
| `--height`       | Height of the maze (number of rows)           | `5`           |
| `--algo`         | Algorithm for generating the maze (`dfs` or `prim`) | `dfs`         |

### Examples

1. **Generate a 10x5 maze using DFS:**
   ```bash
   python main.py --width 10 --height 5 --algo dfs
   ```

2. **Generate a 20x10 maze using Prim's algorithm:**
   ```bash
   python main.py --width 20 --height 10 --algo prim
   ```

---

## 🗂️ Project Structure

```plaintext
maze-generator-solver/
├── maze.py         # Maze generation logic (DFS and Prim's)
├── solver.py       # BFS solver to find the shortest path
├── main.py         # Command-line interface and Tkinter GUI
├── README.md       # Project documentation
```

---

## 🤖 How It Works

1. **Maze Generation:**
   - 🔄 **DFS:** Randomly removes walls between cells using a recursive stack-based backtracking algorithm.
   - ✨ **Prim's:** Incrementally builds the maze by adding neighboring cells and removing walls.
2. **Maze Solving:**
   - 🔀 **BFS:** Ensures the shortest path from the start to the goal is found.
3. **Graphical Display:**
   - Tkinter's Canvas widget draws the maze grid, walls, and highlights the solution path with red dots.

---

## 🎨 Screenshots

### Example: A 10x5 Maze (DFS)

Generated Maze:

```
 _ _ _ _ _ _ _ _ _ _
|_|_  |_  |_  |_  |_|
|_|_|_  |_  |_ _ _|_|
|_|_|_|_ _|_|_|_|_|_|
|_|_|_|_  |_  |_  |_|
|_|_|_|_|_|_|_|_|_|_|
```

GUI Output:
![image](https://github.com/user-attachments/assets/20290846-1f09-4a00-9e5d-e10ce685a99d)


---

## 🌐 Possible Improvements

- Add ⭐ **A*** or 🎮 **Dijkstra's Algorithm** for solving.
- Implement a ⚖️ **maze editor** for manual adjustments.
- Add buttons for 🔄 **real-time generation** and solution visualization.

---

## ℹ️ License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👤 Author

Developed by **[Your Name](https://github.com/<your-username>)**. Feel free to fork, modify, and contribute to this project!

