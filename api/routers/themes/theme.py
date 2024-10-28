
from fastapi import APIRouter 
from fastapi.responses import JSONResponse
import sys


router = APIRouter()

@router.get('/theme')
def user_theme():
    try:
        data = {
             "bg": "red",
            "text": "black",
            "primary": "blue",
            "secondary": "green"
          }
        return JSONResponse(content=data, status_code=200)
    except Exception as e:
        exception_data = sys.exc_info()
        data = {
            'message': e,
            'exception': exception_data
        }
        return JSONResponse(status_code=500, content=data)



        
