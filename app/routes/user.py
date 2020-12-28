from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.ext.db import get_db
from app.services import user as user_service
from app.schemas import user as user_schema

router = APIRouter(prefix='/user', tags=['User'])


@router.get('/', response_model=List[user_schema.UserOut], description='Get list of all users')
def get_all_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return user_service.get_all_users(db=db, skip=skip, limit=limit)


@router.get('/{userid}', response_model=user_schema.UserOut, description='Get user by ID')
def get_user_by_id(db: Session = Depends(get_db), userid: int = None):
    return user_service.get_user_by_id(db, userid)


@router.post('/', response_model=user_schema.UserOut, description='Create a new user')
def create_new_user(db: Session = Depends(get_db), user: user_schema.UserRegister = Depends()):
    return user_service.create_new_user(db, user)


@router.put('/{userid}', response_model=user_schema.UserOut, description='Update user')
def update_user(db: Session = Depends(get_db), userid: int = 0, user: user_schema.UserIn = Depends()):
    return user_service.update_user(db, userid, user)


@router.patch('/{userid}', response_model=user_schema.UserOut, description='Update user fields')
def patch_user(db: Session = Depends(get_db), userid: int = 0, user: user_schema.UserPatch = Depends()):
    return user_service.patch_user(db, userid, user)


@router.delete('/{userid}', description='Delete user', responses={200: {'detail': 'User deleted'}})
def delete_user(db: Session = Depends(get_db), userid: int = 0):
    return user_service.delete_user(db, userid)