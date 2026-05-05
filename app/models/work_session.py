from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from app.database.base import Base

class Work_session(Base):
    __tablename__ ="work_sessions"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(Time)
    end_time = Column(Time)
    date = Column(Date)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)