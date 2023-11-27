from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from environs import Env


@dataclass
class WiseConfig:
    api_token: Optional[str]

    @staticmethod
    def from_env(env: Env):
        api_token = env.str("WISE_API_TOKEN")

        return WiseConfig(
            api_token=api_token,
        )


@dataclass
class Config:
    wise: WiseConfig


def load_config(path: str | Path = None) -> Config:
    """
    This function takes an optional file path as input and returns a Config object.
    :param path: The path of env file from where to load the configuration variables.
    It reads environment variables from a .env file if provided, else from the
    process environment.

    :return: Config object with attributes set as per
    environment variables.
    """

    # Create an Env object.
    # The Env object will be used to read environment variables.
    env = Env()
    env.read_env(path)

    return Config(
        wise=WiseConfig.from_env(env),
    )
