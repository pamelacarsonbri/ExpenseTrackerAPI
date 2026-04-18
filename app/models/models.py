from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.sql import func
from app.database import Base

CATEGORIES = ["Food", "Transport", "Entertainment", "Utilities", "Health", "Other"]

class Expense(Base):
    """Represents a single logged expense."""
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, default=func.current_date())
    category = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)

class Budget(Base):
    """Represents a monthly budget for a category."""
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), nullable=False, unique=True)
    amount = Column(Float, nullable=False)

