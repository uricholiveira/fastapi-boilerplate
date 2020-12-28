from fastapi import FastAPI
import uvicorn
from app.models import generate_models
from app.routes import user as user_route

app = FastAPI()

generate_models()

app.include_router(router=user_route.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
