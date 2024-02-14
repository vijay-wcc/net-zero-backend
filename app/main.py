from fastapi import FastAPI
from app.routers import organization_router

app = FastAPI()

app.include_router(organization_router.router, prefix="/api/v1", tags=["organizations"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
