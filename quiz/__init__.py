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
  max_power: 3
  roots: true
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

class _Config_Dict(typing.TypedDict):
    basic: _BasicModeConfig
    times_table: _TimesTableModeConfig
    advanced: _AdvancedModeConfig

class Config:
    _instance: 'Config' = None # type: ignore
    cf: _Config_Dict = None # type: ignore
    def __new__(cls, cf_dict: typing.Optional[_Config_Dict] = None) -> typing.Self:
        if not cls._instance:
            cls._instance = cls(cf_dict)
            cls._instance.cf = cf_dict # type: ignore
        return cls._instance


def gen_op() -> Operation:
    config = Config()

    BASIC_OPS = ["add", "sub",]
    TT_OPS = ["mul", "div"]
    ADVANCED_OPS = ["pow", "root"]

    avail_ops = []
    if config.cf["basic"]["enable"]:
        avail_ops += BASIC_OPS
    if config.cf["times_table"]["enable"]:
        avail_ops += TT_OPS
    if config.cf["advanced"]["enable"]:
        avail_ops += ADVANCED_OPS

    return random.choice(avail_ops)
