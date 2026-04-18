from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.schemas import ExpenseCreate, ExpenseResponse
from app.services import expense_service

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Log a new expense",
)
def log_expense(data: ExpenseCreate, db: Session = Depends(get_db)):
    """
    Log a new expense entry.

    - **category**: Must be one of: Food, Transport, Entertainment, Utilities, Health, Other
    - **description**: Short note about what was spent on
    - **amount**: Must be greater than 0
    - **date**: Optional — defaults to today if not provided
    """
    return expense_service.create_expense(db, data)

@router.get(
    "/",
    response_model=list[ExpenseResponse],
    summary="Get all expenses",
)
def list_expenses(db: Session = Depends(get_db)):
    """Return all logged expenses, newest first."""
    return expense_service.get_all_expenses(db)

@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    summary="Get a single expense by ID",
)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    """Return a single expense. Returns 404 if not found."""
    return expense_service.get_expense_by_id(db, expense_id)

@router.get(
    "/category/{category}",
    response_model=list[ExpenseResponse],
    summary="Get all expenses in a category",
)
def get_by_category(category: str, db: Session = Depends(get_db)):
    """Return all expenses for the given category."""
    return expense_service.get_expenses_by_category(db, category)

@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete an expense",
)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    """Delete an expense by ID. Returns 404 if not found."""
    return expense_service.delete_expense(db, expense_id)


