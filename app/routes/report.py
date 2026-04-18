from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.schemas import FullReport
from app.services import report_service

router = APIRouter(prefix="/report", tags=["Report"])

@router.get(
    "/",
    response_model=FullReport,
    summary="Get full spending report",
)
def full_report(db: Session = Depends(get_db)):
    """
    Generate a complete spending report including:
    - Total amount spent across all categories
    - Number of expenses logged
    - The single largest expense
    - The category with the highest total spending
    - A breakdown per category: budget set, amount spent, remaining, and over-budget warning
    """
    return report_service.get_full_report(db)


