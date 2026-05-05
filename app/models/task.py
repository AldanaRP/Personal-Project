from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from app.database.base import Base

class Task(Base):
    __tablename__ ="tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    due_date = Column(Date)
    due_time = Column(Time)

    user_id = Column(Integer, ForeignKey("users.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"), nullable=False)