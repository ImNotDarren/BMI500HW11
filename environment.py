from agent import Agent
import random


class Environment:
    def __init__(self, p: float, q: float, grid_size: int = 75, agent_num: int = 100, agent_mode: str = "random"):
        self.agents = []
        self.p = p
        self.q = q
        self.grid_size = grid_size
        self.agent_num = agent_num
        self.agent_mode = agent_mode

    def initialize(self):
        for _ in range(int(0.95 * self.agent_num)):
            x, y = random.randint(0, self.grid_size -
                                  1), random.randint(0, self.grid_size - 1)
            self.agents.append(Agent("S", (x, y), self.agent_mode))

        for _ in range(self.agent_num - len(self.agents)):
            x, y = random.randint(0, self.grid_size -
                                  1), random.randint(0, self.grid_size - 1)
            self.agents.append(Agent("I", (x, y), self.agent_mode))

    def step(self):
        self.walk()
        self.infect()
        self.recover()

    def walk(self):
        for agent in self.agents:
            agent.walk(self.agents)

    def count_infection(self):
        susceptible = 0
        infected = 0
        recovered = 0
        for agent in self.agents:
            if agent.state == "S":
                susceptible += 1
            if agent.state == "I":
                infected += 1
            if agent.state == "R":
                recovered += 1
        return susceptible, infected, recovered

    def infect(self):
        cells = []
        for i in range(len(self.agents)):
            agent = self.agents[i]
            curr_cell = agent.position
            if curr_cell in cells:
                continue

            cells.append(curr_cell)
            curr_cell_agents = [i]
            has_infected = False
            for j in range(len(self.agents)):
                if j != i and self.agents[j].position == curr_cell:
                    curr_cell_agents.append(j)
                    if self.agents[j].state == "I":
                        has_infected = True
            if has_infected:
                for a in curr_cell_agents:
                    if random.random() < self.p and self.agents[a].state == "S":
                        self.agents[a].state = "I"

    def recover(self):
        for agent in self.agents:
            if agent.state == "I" and random.random() < self.q:
                agent.state = "R"
