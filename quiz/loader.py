import yaml
import typing

from . import *
from . import _Config_Dict

def load_config() -> _Config_Dict:
    def _load() -> dict[str, typing.Any]:
        return yaml.safe_load(CONFIG_PATH)
    
    try:
        cfg = _load()
    except FileNotFoundError:
        with open(CONFIG_PATH, "w") as f:
            f.write(SAMPLE_CONFIG)
        cfg = _load()
    
    if any((itm_name := item)
            not in cfg
                for item in ["basic", "times_table", "advanced"]):
        raise InvalidConfigError(itm_name)

    if any((itm_name := item)
            not in cfg["basic"]
                for item in ["enable", "imperfect_digits", "max"]):
        raise InvalidConfigError(f"basic.{itm_name}")
    
    if any((itm_name := item)
            not in cfg["times_table"]
                for item in ["enable", "up_to"]):
        raise InvalidConfigError(f"times_table.{itm_name}")

    if any((itm_name := item)
            not in cfg["advanced"]
                for item in ["enable", "max_base", "max_power", "roots"]):
        raise InvalidConfigError(f"advanced.{itm_name}")

    return cfg # type: ignore
