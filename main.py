from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api.routers.user_operations import user_router

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],  # Specify methods if you only want to allow certain ones
    allow_headers=["*"],  # Specify headers if required
)

app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9000, reload=True)
