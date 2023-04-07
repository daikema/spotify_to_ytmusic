import configparser
from pathlib import Path
from typing import Optional


class Settings:

    config: configparser.ConfigParser
    def __init__(self, filepath: Optional[Path] = None):
        self.config = configparser.ConfigParser(interpolation=None)
        self.filepath = filepath if filepath else Path(__file__).parent.joinpath('settings.ini')
        self.config.read(self.filepath)

    def __getitem__(self, key):
        return self.config[key]

    def __setitem__(self, section, key, value):
        self.config.set(section, key, value)

    def save(self):
        with open(self.filepath, 'w') as f:
            self.config.write(f)