import uvicorn
from fastapi import FastAPI

from safecity_platform.api.auth_controller import auth_router
from safecity_platform.api.incident_controller import incident_router

app = FastAPI()
app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=incident_router, prefix="/incident")
if __name__ == "__main__":
    uvicorn.run("safecity_platform.main:app", host="127.0.0.1", port=8001, reload=True)