import yaml
import colorama
import typing

from . import *

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
    max_power: int
    roots: bool

class Config(typing.TypedDict):
    enable: list[Mode]
    basic: _BasicModeConfig
    times_table: _TimesTableModeConfig
    advanced: _AdvancedModeConfig


def load_config() -> Config:
    cfg: dict[str, typing.Any] = yaml.safe_load("./quiz_config.yaml")
    
