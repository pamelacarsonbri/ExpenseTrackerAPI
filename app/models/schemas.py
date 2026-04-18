from pydantic import BaseModel, Field, field_validator
from datetime import date as date_type
from typing import Optional
from app.models.models import CATEGORIES

# ── Expense Schemas ────────────────────────────────────────────────────────────

class ExpenseCreate(BaseModel):
    category: str = Field(..., examples=["Food"])
    description: str = Field(..., examples=["Lunch at KFC"])
    amount: float = Field(..., gt=0, examples=[45.50])
    date: Optional[date_type] = Field(default=None, examples=["2026-03-16"])

    @field_validator("category") 
    @classmethod
    def validate_category(cls, value: str) -> str:
        if value not in CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(CATEGORIES)}")
        return value

class ExpenseResponse(BaseModel):
    id: int
    date: date_type
    category: str
    description: str
    amount: float

    model_config = {"from_attributes": True}

# ── Budget Schemas ─────────────────────────────────────────────────────────────

class BudgetCreate(BaseModel):
    category: str = Field(..., examples=["Food"])
    amount: float = Field(..., gt=0, examples=[200.00])

    @field_validator("category")
    @classmethod
    def validate_category(cls, value: str) -> str:
        if value not in CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(CATEGORIES)}")
        return value

class BudgetResponse(BaseModel):
    id: int
    category: str
    amount: float

    model_config = {"from_attributes": True}

# ── Summary / Report Schemas ───────────────────────────────────────────────────

class CategorySummary(BaseModel):
    category: str
    budget: float
    spent: float
    remaining: float
    over_budget: bool

class FullReport(BaseModel):
    total_spent: float
    number_of_expenses: int
    largest_expense: Optional[ExpenseResponse]
    highest_spending_category: Optional[str]
    category_summaries: list[CategorySummary]


