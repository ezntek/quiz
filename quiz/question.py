from . import Operation
from dataclasses import dataclass

class Question:
    def __init__(self, values: tuple[int, int]):
        self.op: Operation = gen_op()
        self.values: tuple[int, int] = values

