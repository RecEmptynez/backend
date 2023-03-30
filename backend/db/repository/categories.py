from sqlalchemy.orm import Session
from sqlalchemy import Insert
from db.models.categories import Category

def insert_category(category_name:str,db:Session):
    insert_stmt = Insert(Category).values(title=category_name).returning(Category.id,Category.title)
    result = db.execute(insert_stmt).fetchall()
    db.commit()
    return result[0]