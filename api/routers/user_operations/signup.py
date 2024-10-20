from database.models import UserInfo
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database.db_session import get_db
from argon2 import PasswordHasher
import sys
from .utils import generate_api_key
class NewUser(BaseModel):
    username: Optional[str] = None
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    org_name: Optional[str] = None
    org_logo: Optional[str] = None

router = APIRouter()
hash_pass = PasswordHasher()

@router.post("/signup")
def create_user(args: NewUser, SESSION:Session = Depends(get_db)):
    try:        
        is_existing_user = SESSION.query(UserInfo).filter(args.email == UserInfo.email).first()
        if is_existing_user:
            return JSONResponse(status_code=400, content='User account already registered')
        if args.username:
            is_username_taken = SESSION.query(UserInfo).filter(args.username == UserInfo.username).first()
            if is_username_taken:
                return JSONResponse(status_code=400, content='Username Taken')
        new_user_data = {
            'username': args.username,
            'email': args.email,
            'password': hash_pass.hash(args.password),
            'first_name': args.first_name,
            'last_name': args.last_name,
            'address': args.address,
            'org_name': args.org_name,
            'org_logo': args.org_logo,
            'api_key': generate_api_key()
        }

        new_user = UserInfo(**new_user_data)
        SESSION.add(new_user)
        SESSION.commit()
        return JSONResponse(content='User created successfully', status_code=200)

    except Exception as e:
        SESSION.rollback()
        exception_data = sys.exc_info()
        data = {
            'message': e,
            'exception': exception_data
        }
        return JSONResponse(status_code=500, content=data)
    finally:
        SESSION.close()

    