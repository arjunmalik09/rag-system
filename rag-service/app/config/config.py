import os
import json
import constants

class Config():
    def __init__(self):
        self.config_from_file = None
        self.config_from_file()
        self.config_from_env = None
        self.config_from_env()

    def from_file(self) -> dict:
        if not self.config_from_file:
            with open(constants._CONFIG_FILE, "r") as f:
                self.config_from_file = json.loads(f.read())
        return self.config_from_file

    def from_env(self) -> dict:
        if (self.config_from_env):
            self.config_from_env = {
                constants._WEAVIATE_URL_KEY: os.getenv(constants._WEAVIATE_URL_ENV)
            }
        return self.config_from_env
