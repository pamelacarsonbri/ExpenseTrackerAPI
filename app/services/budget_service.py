from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.models import Budget
from app.models.schemas import BudgetCreate

def set_budget(db: Session, data: BudgetCreate) -> Budget:
    """Create or update the budget for a category."""
    existing = db.query(Budget).filter(Budget.category == data.category).first()
    if existing:
        existing.amount = data.amount
        db.commit()
        db.refresh(existing)
        return existing

    budget = Budget(category=data.category, amount=data.amount)
    db.add(budget)
    db.commit()
    db.refresh(budget)
    return budget

def get_all_budgets(db: Session) -> list[Budget]:
    """Return all category budgets."""
    return db.query(Budget).all()

def get_budget_by_category(db: Session, category: str) -> Budget:
    """Return budget for a specific category, or raise 404."""
    budget = db.query(Budget).filter(Budget.category == category).first()
    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No budget set for category '{category}'."
        )
    return budget


