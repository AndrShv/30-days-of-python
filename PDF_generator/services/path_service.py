import os

HOST_USER_DIR = os.getenv("HOST_USER_DIR", "/Users/andrshv")
CONTAINER_USER_DIR = os.getenv("CONTAINER_USER_DIR", "/app/host_user")


def resolve_file_path_for_celery(user_file_path: str) -> str:
    normalized_path = os.path.normpath(user_file_path)

    if normalized_path.startswith(HOST_USER_DIR):
        relative_path = os.path.relpath(normalized_path, HOST_USER_DIR)
        return os.path.join(CONTAINER_USER_DIR, relative_path)

    return normalized_path