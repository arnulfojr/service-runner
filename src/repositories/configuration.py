from cerberus import Validator
from repositories.schemas import CONFIG_SCHEMA


def validate(configuration: dict) -> (bool, list):
    """Validate the config with the config schema."""
    config_validator = Validator(CONFIG_SCHEMA)
    status = config_validator.validate(configuration)

    return status, config_validator.errors
