"""Utility definitions."""


def load_yaml(path: str) -> dict:
    import yaml
    with open(path, mode='r') as f:
        configuration = yaml.safe_load(f)
    return configuration


def load_json(path: str) -> dict:
    import ujson as json
    with open(path, mode='r') as f:
        configuration = json.load(f)
    return configuration
