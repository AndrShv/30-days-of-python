import os

HOST_USER_DIR = "/Users/andrshv"
CONTAINER_USER_DIR = "/app/host_user"


def resolve_file_path_for_celery(user_file_path: str) -> str:
    if user_file_path.startswith(HOST_USER_DIR):
        relative_path = os.path.relpath(user_file_path, HOST_USER_DIR)
        return os.path.join(CONTAINER_USER_DIR, relative_path)
    return user_file_path