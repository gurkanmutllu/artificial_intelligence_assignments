

from a_star import AStar
from maze import Maze


if __name__ == "__main__":
    maze = Maze("maze3.txt")
    print("Maze: ")
    maze.print()
    print("Solving...")
    aStar = AStar(maze)
    aStar.solve()

    maze.solution = aStar.solution
    maze.print()
    aStar.output_image("solved.png")
