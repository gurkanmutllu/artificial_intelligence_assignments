import heapq
import math
from PIL import Image, ImageDraw, ImageFont


class AStar:

    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.goal = maze.goal
        self.explored = set()
        self.solution = None

    def heuristic(self, node):
        return math.sqrt((node[0] - self.goal[0]) ** 2 + (node[1] - self.goal[1]) ** 2)

    def solve(self):
        open_list = [(0, self.start, [])]

        while open_list:
            cost, current, path = heapq.heappop(open_list)

            if current == self.goal:
                self.solution = (cost, path + [current])
                return

            if current in self.explored:
                continue

            self.explored.add(current)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = current[0] + dr, current[1] + dc
                if 0 <= r < self.maze.height and 0 <= c < self.maze.width and not self.maze.walls[r][c]:
                    new_cost = cost + 1
                    new_path = path + [current]
                    heapq.heappush(
                        open_list, (new_cost + self.heuristic((r, c)), (r, c), new_path))

    def output_image(self, filename, show_solution=True, show_explored=True):
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.maze.width * cell_size, self.maze.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.maze.solution[1] if self.maze.solution is not None else None
        font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20)

        for i, row in enumerate(self.maze.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.maze.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.maze.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
                # draw.text(
                #     (j * cell_size + cell_border, i * cell_size + cell_border),
                #     str(self.costs[j][i]), font=font)

        img.save(filename)
