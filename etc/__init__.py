import os
import yaml

__all__ = ["settings"]

DIR = f"{os.getcwd()}/etc/settings.yaml"
SETTINGS = None

with open(DIR, 'r') as stream:
    try:
        SETTINGS = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)