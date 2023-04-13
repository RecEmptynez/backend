from sqlalchemy import Column, Integer, String
from db.base_class import Base

#Creates reflection of the table recipes in the database
class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer,primary_key = True,autoincrement=True, index=True)
    title = Column(String,nullable= False)
    url = Column(String,nullable= False)
    difficulty = Column(String, nullable=False)
    picture_url = Column(String,nullable= False)
    rating = Column(String,nullable= False)