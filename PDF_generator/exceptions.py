from http.client import HTTPException


class ProductNotFoundException(HTTPException):
    def __init__(self, product_id: float):
        super().__init__(f"Product with ID {product_id} not found")


class FileNotFoundByPathException(Exception):
    def __init__(self, path: str):
        super().__init__(f"File with path {path} not found")


class FileNotFoundByIdException(Exception):
    def __init__(self, file_id: str):
        super().__init__(f"File with ID {file_id} not found")