from dotenv import load_dotenv, find_dotenv
from starlette.config import Config


ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)

# https://www.starlette.io/config/
# The order in which configuration values are read is:
# * From an environment variable.
# * From the ".env" file.
# * The default value given in config.
config = Config(ENV_FILE)


######## APP ########
PORT: int = config.get(key="PORT", cast=int, default=8000)
RELOAD: bool = config.get(key="RELOAD", cast=bool, default=False)


######## DB CONFIG ########
DB_DRIVERNAME = config.get(key='DB_DRIVERNAME', cast=str, default='postgresql')
DB_HOST: str = config.get(key='DB_HOST', cast=str, default='localhost')
DB_USER: str = config.get(key='DB_USER', cast=str)
DB_PASSWORD: str = config.get(key='DB_PASSWORD', cast=str)
DB_PORT: int = config.get(key='DB_PORT', cast=int)
DATABASE: str = config.get(key='DATABASE', cast=str, default='sistema_inclusiones')
