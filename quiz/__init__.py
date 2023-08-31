import random
import colorama
import typing

CONFIG_PATH = "./quiz_config.yaml"
SAMPLE_CONFIG = """basic:
  enable: true
  imperfect_digits: true
  max: 30
times_table:
  enable: true
  up_to: 12
advanced:
  enable: true
  max_base: 10
  max_power: 3
  roots: true
count: 20
"""

Operation = typing.Literal["add", "sub", "mul", "div", "pow", "root"]
Mode = typing.Literal['basic', 'times_table', 'advanced']

class InvalidConfigError(Exception):
    """Represents an invalid config file"""
    def __init__(self, key: str) -> None:
        super().__init__(f"{colorama.Style.BRIGHT}{colorama.Back.RED}{key}{colorama.Back.RESET} does not exist in the config. Please do refer to the sample for more information.{colorama.Style.RESET_ALL}")

class _BasicModeConfig(typing.TypedDict):
    enable: bool
    imperfect_digits: bool
    max: int

class _TimesTableModeConfig(typing.TypedDict):
    enable: bool
    up_to: int

class _AdvancedModeConfig(typing.TypedDict):
    enable: bool
    max_base: int
    max_power: int
    roots: bool

class Config(typing.TypedDict):
    basic: _BasicModeConfig
    times_table: _TimesTableModeConfig
    advanced: _AdvancedModeConfig
    count: int

def gen_op(config: Config) -> Operation:
    BASIC_OPS = ["add", "sub",]
    TT_OPS = ["mul", "div"]
    ADVANCED_OPS = ["pow", "root"]

    avail_ops = []
    if config["basic"]["enable"]:
        avail_ops += BASIC_OPS
    if config["times_table"]["enable"]:
        avail_ops += TT_OPS
    if config["advanced"]["enable"]:
        avail_ops += ADVANCED_OPS

    return random.choice(avail_ops)
