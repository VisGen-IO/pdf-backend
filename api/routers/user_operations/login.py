from database.models import UserInfo
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database.db_session import get_db
from argon2 import PasswordHasher, exceptions as argon2_exceptions
import sys
from .utils import is_valid_email, generate_access_token
class LoginModel(BaseModel):
    id: str
    password: str

router = APIRouter()
hash_pass = PasswordHasher()

@router.post('/login')
def user_login(args: LoginModel, SESSION:Session=Depends(get_db)):
    try:
        
        user_obj = SESSION.query(UserInfo).filter(or_(UserInfo.email == args.id, UserInfo.username == args.id)).first()
        if not user_obj:
            return JSONResponse(status_code=404, content='Wrong user id or password')
        try:
            hash_pass.verify(user_obj.password, args.password)
        except argon2_exceptions.VerifyMismatchError:
            return JSONResponse(status_code=404, content="Wrong user id or password")
        data = {
            'access_token': generate_access_token(user_obj.api_key, user_obj.tenant_id)
        }
        return JSONResponse(content=data, status_code=200)
    except Exception as e:
        exception_data = sys.exc_info()
        data = {
            'message': e,
            'exception': exception_data
        }
        return JSONResponse(status_code=500, content=data)
    
@router.post('/reset_password')
def reset_password():
    pass
    




        
