from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from blog import models, schemas
from ..repository import blog
from blog.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from blog.hashing import Hash

router = APIRouter(tags=["blogs"], prefix="/blog")


@router.get('/', response_model=List[schemas.ShowBlog], )
def all_blog(db: SessionLocal = Depends(get_db)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.get('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog, )
def show(id: int, response: Response, db: SessionLocal = Depends(get_db)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, )
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, )
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)
