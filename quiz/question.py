import math
import random

from . import Config, gen_op
from . import Operation

def _gen_vals(op: Operation, config: Config) -> tuple[int, int]:
    match op:
        case "add" | "sub":
            max_val = config["basic"]["max"]
            if not config["basic"]["imperfect_digits"]:
                displacement = random.randint(0, 9)
                val = math.ceil(random.randint(0, max_val)) / (10 ** (len(str(max))-1))
                return (val - displacement, displacement)
            else:
                val = random.randint(0, max_val)
                return (val, val)
    
        case "mul" | "div":
            up_to = config["times_table"]["up_to"]
            val1 = random.randint(0, up_to)
            val2 = random.randint(0, up_to)

            return (val1, val2)
        case "pow":
            base = random.randint(0, config["advanced"]["max_base"])
            pow = random.randint(2, config["advanced"]["max_power"])

            return (base, pow)
        case "root":
            PERFECT_SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            PERFECT_CUBES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            if random.randint(0, 10) % 2:
                return (random.choice(PERFECT_SQUARES), 2)
            else:
                return (random.choice(PERFECT_CUBES), 3)

def _repr_op(op: Operation) -> str:
    return {
        "add": "+",
        "sub": "-", 
        "mul": "*", 
        "div": "/", 
        "pow": "^", 
        "root": "√", 
    }[op]

class Question:
    def __init__(self, config: Config):
        self._config = config
        self.op: Operation = gen_op(self._config)
        self.values: tuple[int, int] = _gen_vals(self.op, self._config)

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
    
    def __repr__(self) -> str:
        if self.op == "root":
            return f"{self.values[1]}{_repr_op(self.op)}{self.values[0]}"
        return f"{self.values[0]}{_repr_op(self.op)}{self.values[1]}"
