from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database.base import Base

class Project_task(Base):
    __tablename__ ="project_tasks"

    id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    date_completed = Column(Date, primary_key=True)

    status_id = Column(Integer, ForeignKey("statuses.id"), nullable=False)