from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Project(Base):
    __tablename__ ="projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    difficulty = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)