from datetime import date as date_type
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.models import Expense
from app.models.schemas import ExpenseCreate

def create_expense(db: Session, data: ExpenseCreate) -> Expense:
    """Log a new expense to the database."""
    expense = Expense(
        date=data.date or date_type.today(),
        category=data.category,
        description=data.description,
        amount=data.amount,
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_all_expenses(db: Session) -> list[Expense]:
    """Return all expenses ordered by date descending."""
    return db.query(Expense).order_by(Expense.date.desc()).all()

def get_expense_by_id(db: Session, expense_id: int) -> Expense:
    """Return a single expense by ID, or raise 404."""
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found."
        )
    return expense

def get_expenses_by_category(db: Session, category: str) -> list[Expense]:
    """Return all expenses for a given category."""
    return db.query(Expense).filter(Expense.category == category).order_by(Expense.date.desc()).all()

def delete_expense(db: Session, expense_id: int) -> dict:
    """Delete an expense by ID, or raise 404."""
    expense = get_expense_by_id(db, expense_id)
    db.delete(expense)
    db.commit()
    return {"message": f"Expense '{expense.description}' deleted successfully."}


