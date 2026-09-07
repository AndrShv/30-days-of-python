from http.client import HTTPException

from starlette import status


class FileNotFoundByPathException(HTTPException):
    def __init__(self, path: str):
        super().__init__(f"File with path {path} not found")


class FileNotFoundByIdException(HTTPException):
    def __init__(self, file_id: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"File with ID {file_id} not found")