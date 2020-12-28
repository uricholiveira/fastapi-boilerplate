from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.models import generate_models
from app.routes import user as user_route

app = FastAPI()

generate_models()

app.include_router(router=user_route.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
