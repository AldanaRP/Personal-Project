from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database.base import Base

class Habit_log(Base):
    __tablename__ ="habit_logs"

    habit_id = Column(Integer, ForeignKey("habits.id"), primary_key=True)
    date_completed = Column(Date, primary_key=True)

    status_id = Column(Integer, ForeignKey("statuses.id"), nullable=False)