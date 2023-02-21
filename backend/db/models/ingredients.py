from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

#Creates reflection of the table categories in the database
class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer,autoincrement=True,primary_key = True, index=True)
    title = Column(String,nullable= False)
    category_id = Column(Integer,ForeignKey("categories.id"),nullable= False)
