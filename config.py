import os


def str2bool(value):
    return value.lower() in ('yes', 'true', 't', '1')


def env_var(name, converter=None, default=None):
    value = os.environ.get(name)
    if value is None or (isinstance(value, str) and len(value) == 0):
        return default
    elif converter:
        return converter(value)
    else:
        return value


DEBUG = env_var('DEBUG', str2bool, False)
USE_RELOADER = env_var('USE_RELOADER', str2bool, False)
PORT = env_var('PORT', int, 5000)
