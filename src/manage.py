#!/usr/bin/env python
import sys




def env_path():
    from pathlib import Path
    env_path = Path('..') / '.env'
    return env_path


if __name__ == '__main__':
    from dotenv.main import DotEnv

    env_path = env_path()
    print(f"* Env Path: {env_path}")

    dotenv = DotEnv(env_path, verbose=False)
    dotenv_dict = dotenv.dict()
    print("* Loaded Env")
    for k, v in dotenv_dict.items():
        print(f'** {k}={v}')
    dotenv.set_as_environment_variables(override=True)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
