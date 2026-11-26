
import uvicorn
from fastapi import FastAPI

from celery_example.tasks import fast_api_app

app = FastAPI(title="Celery + FastAPI Demo")
app.include_router(router=fast_api_app)


if __name__ == "__main__":
    uvicorn.run("celery_example.main:app", host="127.0.0.1", port=8001, reload=True)