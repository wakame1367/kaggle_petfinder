import os


def is_script_running():
    script_only_env_keys = {'KAGGLE_DOCKER_IMAGE', 'KAGGLE_CONTAINER_NAME'}
    current_os_env = set(os.environ.keys())
    is_script = script_only_env_keys.issubset(current_os_env)
    return is_script
