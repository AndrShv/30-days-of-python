import uvicorn
from fastapi import FastAPI

from PDF_generator.rest.file_rest import file_router

app = FastAPI(title="PDF Generator API", version="1.0.0")
app.include_router(router=file_router)

if __name__ == "__main__":
    uvicorn.run("PDF_generator.main:app", host="127.0.0.1", port=8001, reload=True)