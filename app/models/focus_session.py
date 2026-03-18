from sqlalchemy import Column, Integer, String, Date, Time
from app.database.base import Base

class Task(Base):
    __tablename__ ="tasks"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(Time)
    end_time = Column(Time)
    date = Column(Date)
    
    user_id = Column(Integer, ForeignKey("users.id"))