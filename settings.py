import json
import os
import environ

env = environ.Env(
    DEBUG=(bool, False),
)

environ.Env.read_env()

ENV_MODE = env("ENV_MODE", default="production")

if ENV_MODE == 'local':
    with open('env.json') as json_env_file:
        json_env = json.load(json_env_file)
        os.environ.update(json_env)

DEBUG_MODE = env.bool("DEBUG_MODE", default=False)
DB_URL = env("DB_URL", default="postgresql://vision:lXvUXya6hrO09Oqg0Egf6WEiNFEK2Fqh@dpg-cs7adrlds78s73b9gddg-a.virginia-postgres.render.com/vision_g9nk")