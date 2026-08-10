import configparser
import tempfile
import os

config = configparser.ConfigParser()
config["DEFAULT"] = {"timeout": "30", "retries": "3"}
config["database"] = {
    "host": "localhost",
    "port": "5432",
    "name": "mydb",
}
config["api"] = {
    "key": "abc123",
    "base_url": "https://api.example.com",
}

config_file = os.path.join(tempfile.gettempdir(), "config.ini")
with open(config_file, "w") as f:
    config.write(f)

loaded = configparser.ConfigParser()
loaded.read(config_file)

print("DB host:", loaded["database"]["host"])
print("DB port:", loaded["database"]["port"])
print("Timeout:", loaded["database"]["timeout"])
print("Sections:", loaded.sections())

os.remove(config_file)
