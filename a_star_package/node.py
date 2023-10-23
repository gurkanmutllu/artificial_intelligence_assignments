
class Node:
    def __init__(self, position, parent, cost_to_reach, estimated_cost_to_goal):
        self.position = position
        self.parent = parent
        self.cost_to_reach = cost_to_reach
        self.estimated_cost_to_goal = estimated_cost_to_goal

    def __lt__(self, other):
        # Bu, heapq'nin öncelik sırasını belirlemek için kullanılır.
        return (self.cost_to_reach + self.estimated_cost_to_goal) < (other.cost_to_reach + other.estimated_cost_to_goal)
