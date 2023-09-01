import math
import random

from . import Config, gen_op
from . import Operation

def _gen_vals(op: Operation, config: Config) -> tuple[int, int]:
    match op:
        case "add" | "sub":
            max_val = config["basic"]["max"]
            if not config["basic"]["imperfect_digits"]:
                displacement = random.randint(1, 9)  # calculate the displacement from the nearest 10
                val = round(random.randint(0, max_val+5), -1) # get a value rounded to the nearest 10
                return (val - displacement, displacement)
            else:
                lim = math.floor(max_val/2)
                val1 = random.randint(0, lim)
                val2 = random.randint(0, val1) # ensure no negative results
                return (val1, val2)
        case "mul":
            up_to = config["times_table"]["up_to"]
            val1 = random.randint(2, up_to)
            val2 = random.randint(2, up_to)

            return (val1, val2)
        case "div":
            up_to = config["times_table"]["up_to"]

            # generate a times table with key being the number and a list of values ranging from num*1..limit
            TIMES_TABLE = {i+1: [(i+1)*(j+1) for j in range(up_to)] for i in range(up_to)}
            
            divisor = random.randint(2, up_to)
            dividend = random.choice(TIMES_TABLE[divisor])
            return (dividend, divisor)
        case "pow":
            base = random.randint(1, config["advanced"]["max_base"])
            pow = random.randint(2, config["advanced"]["max_power"])

            return (base, pow)
        case "root":
            # hard-code perfect squares and cubes
            PERFECT_SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            PERFECT_CUBES = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
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
                return round(self.values[0] ** (1/self.values[1]))
    
    def __repr__(self) -> str:
        if self.op == "root":
            # dont show the nth root if it is a square root
            if self.values[1] == 2:
                return f"{_repr_op(self.op)}{self.values[0]}"

            # n√x where n is the root and x is the number
            return f"{self.values[1]}{_repr_op(self.op)}{self.values[0]}"
        
        # a<operation>b
        return f"{self.values[0]}{_repr_op(self.op)}{self.values[1]}"
