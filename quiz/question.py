import math
import random

from . import Config, gen_op
from . import Operation

def _gen_vals(op: Operation) -> tuple[int, int]:
    config = Config()
    match op:
        case "add" | "sub":
            max_val = config.cf["basic"]["max"]
            if not config.cf["basic"]["imperfect_digits"]:
                val = random.randint(0, max_val)
                return (val, val)
            else:
                displacement = random.randint(0, 9)
                val = math.ceil(random.randint(0, max_val)) / (10 ** (len(str(max))-1))
                return (val - displacement, displacement)
        case "mul" | "div":
            up_to = config.cf["times_table"]["up_to"]
            val1 = random.randint(0, up_to)
            val2 = random.randint(0, up_to)

            return (val1, val2)
        case "pow":
            base = random.randint(0, config.cf["advanced"]["max_base"])
            pow = random.randint(2, config.cf["advanced"]["max_power"])

            return (base, pow)
        case "root":
            PERFECT_SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            PERFECT_CUBES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            if random.randint(0, 10) % 2:
                return (random.choice(PERFECT_SQUARES), 2)
            else:
                return (random.choice(PERFECT_CUBES), 3)

class Question:
    def __init__(self):
        self._config = Config()
        self.op: Operation = gen_op()
        self.values: tuple[int, int] = _gen_vals(self.op)

    def solve(self) -> int:
        match self.op:
            case "add":
                return self.values[0] + self.values[1]
            case "sub":
                return self.values[0] - self.values[1]
            case "mul":
                return self.values[0] * self.values[1]
            case "div":
                return math.floor(self.values[0] / self.values[1])
            case "pow":
                return self.values[0] ** self.values[1]
            case "root":
                return math.floor(self.values[0] ** (1/self.values[1]))
