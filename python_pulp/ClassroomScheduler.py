from pulp import *
from datetime import datetime

# Create model
m = LpProblem("Classroom Scheduler", 0)

# Generate 5-minute blocks for 24 hour period
blocks = [str(datetime(2018, 1, 1, hr, min, 0).time()) for hr in range(0, 24) for min in range(0, 60, 5)]

print(blocks)


class Block:
    def __init__(self, start_dtm):
        self.start_dtm = start_dtm


