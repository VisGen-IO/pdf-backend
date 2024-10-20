from fastapi import FastAPI
import uvicorn
from api.routers.user_operations import user_router

app = FastAPI()

app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(app, host=9000, reload=True)