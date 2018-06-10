import configparser
import os


class ConfigManager(object):
    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        if os.path.exists(filename) is not True:
            print("Error: cannot find config file %s" % filename)
        else:
            print("load config file %s" % filename)
        self.config.read(filename)

    def config_get(self, option, item):
        return self.config.get(option, item)

    def config_set(self, option, item, value):
        self.config.set(option, item, value)
        if self.config.get(option, item) != str(value):
            return False
        return True
