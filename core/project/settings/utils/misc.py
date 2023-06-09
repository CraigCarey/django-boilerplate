import yaml


def yaml_coerce(value):
    # convert value to proper Python

    if isinstance(value, str):
        # yaml load returns a Python object (we are just creating some quick yaml data with a dummy value)
        # Converts string dict "{'apples': 1, 'bacon': 2}" to Python dict
        # Useful because sometimes we need to stringify settings this way (e.g. in Dockerfiles)
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
