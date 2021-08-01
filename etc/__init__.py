import yaml

__all__ = ["settings"]

SETTINGS = None
with open("/home/nefta/Documentos/PROJECTS/cargamosShop/etc/settings.yaml", 'r') as stream:
    try:
        SETTINGS = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)