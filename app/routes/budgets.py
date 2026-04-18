from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.schemas import BudgetCreate, BudgetResponse
from app.services import budget_service

router = APIRouter(prefix="/budgets", tags=["Budgets"])

@router.post(
    "/",
    response_model=BudgetResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Set or update a category budget",
)
def set_budget(data: BudgetCreate, db: Session = Depends(get_db)):
    """
    Set or update the monthly budget for a category.
    If a budget already exists for the category, it will be updated.

    - **category**: Must be one of: Food, Transport, Entertainment, Utilities, Health, Other
    - **amount**: Monthly budget amount in GHS
    """
    return budget_service.set_budget(db, data)

@router.get(
    "/",
    response_model=list[BudgetResponse],
    summary="Get all budgets",
)
def list_budgets(db: Session = Depends(get_db)):
    """Return all category budgets."""
    return budget_service.get_all_budgets(db)

@router.get(
    "/{category}",
    response_model=BudgetResponse,
    summary="Get budget for a specific category",
)
def get_budget(category: str, db: Session = Depends(get_db)):
    """Return the budget for a specific category. Returns 404 if not set."""
    return budget_service.get_budget_by_category(db, category)


