import os

import configparser

from pytz import timezone as tz
from loguru import logger

timezone = tz('Europe/London')


# Detect if running in a container (ECS sets this)
IN_CONTAINER = os.getenv('AWS_EXECUTION_ENV') is not None


# Load config file ONLY if not in container
config = {}
if not IN_CONTAINER:
    logger.info('Local environment detected, loading config from envfile.ini')
    parser = configparser.ConfigParser()
    parser.read('envfile.ini', encoding='utf-8')
    config = parser['DEFAULT']
else:
    logger.info('AWS Container environment detected, loading config from environment variables.')


def get_setting(key: str, default: str | None = None, required: bool = True):
    """
    Priority:
    1. Environment variables (ECS, Docker runtime)
    2. envfile.ini (local development)
    3. Default (if provided)
    """
    # 1. Try environment variable first
    value = os.getenv(key)

    # 2. Fall back to config file (local only)
    if value is None and config:
        value = config.get(key, fallback=default) # type: ignore

    # 3. Fall back to default
    if value is None:
        if required:
            raise ValueError(f'Missing required configuration: {key}')

        logger.info(f'No value found for {key} using default.')
        value = default
    else:
        logger.info(f'Loaded environment variable {key}')

    return value


# --- Application settings ---
JWT_ACCESS_SECRET = get_setting('JWT_ACCESS_SECRET', None, True)
JWT_REFRESH_SECRET = get_setting('JWT_REFRESH_SECRET', None, True)
PG_USERNAME = get_setting('PG_USERNAME', None, True)
PG_PASSWORD = get_setting('PG_PASSWORD', None, True)
PG_HOST = get_setting('PG_HOST', None, True)
PG_PORT = get_setting('PG_PORT', None, True)
PG_DATABASE = get_setting('PG_DATABASE', None, True)
test = get_setting('test-secret-manager', 'did not read :(', False)

logger.info(f'Loaded test variable: {test}')
