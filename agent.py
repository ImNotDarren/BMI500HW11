import numpy as np
import random


class Agent:
    def __init__(self, state: str, position: tuple, mode: str = "random"):
        self.state = state
        self.position = position
        self.mode = mode

    def walk(self, agents):
        if self.mode == "random":
            self.random_walk()
            return

        self.smart_walk(agents)

    def random_walk(self):
        x, y = self.position
        new_x = x + random.choice([-1, 0, 1])
        new_y = y + random.choice([-1, 0, 1])
        if new_x >= 0 and new_x < 75 and new_y >= 0 and new_y < 75:
            self.position = (new_x, new_y)

    def smart_walk(self, agents):
        if self.state == "I" or self.state == "R":
            self.random_walk()
            return

        x, y = self.position
        min_dist = float("inf")
        nearest_agent = None
        for agent in agents:
            if agent.state == "I":
                i, j = agent.position
                dist = np.sqrt((x - i) ** 2 + (y - j) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    nearest_agent = agent

        if nearest_agent is None:
            self.random_walk()
            return

        i, j = nearest_agent.position
        new_x = x - random.choice([0, 1]) if x < i else x + \
            random.choice([0, 1])
        new_y = y - random.choice([0, 1]) if y < j else y + \
            random.choice([0, 1])
        if new_x >= 0 and new_x < 75 and new_y >= 0 and new_y < 75:
            self.position = (new_x, new_y)
