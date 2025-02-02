from fastapi import FastAPI
from src.routes.workspace_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Workspace List Service is Running"}
