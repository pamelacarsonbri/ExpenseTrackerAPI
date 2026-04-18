from sqlalchemy.orm import Session
from app.models.models import Expense, Budget, CATEGORIES
from app.models.schemas import CategorySummary, FullReport, ExpenseResponse

def get_full_report(db: Session) -> FullReport:
    """
    Generate a full spending report:
    - Grand total spent
    - Largest single expense
    - Highest spending category
    - Per-category budget vs spent breakdown
    """
    expenses = db.query(Expense).all()
    budgets = {b.category: b.amount for b in db.query(Budget).all()}

    total_spent = sum(e.amount for e in expenses)
    number_of_expenses = len(expenses)

    largest_expense = None
    if expenses:
        top = max(expenses, key=lambda e: e.amount)
        largest_expense = ExpenseResponse.model_validate(top)

    # Tally spend per category
    category_totals: dict[str, float] = {c: 0.0 for c in CATEGORIES}
    for e in expenses:
        if e.category in category_totals:
            category_totals[e.category] += e.amount

    highest_spending_category = None
    if any(v > 0 for v in category_totals.values()):
        highest_spending_category = max(category_totals, key=category_totals.get)

    category_summaries = []
    for category in CATEGORIES:
        spent = category_totals[category]
        budget = budgets.get(category, 0.0)
        remaining = budget - spent
        category_summaries.append(CategorySummary(
            category=category,
            budget=budget,
            spent=spent,
            remaining=remaining,
            over_budget=spent > budget and budget > 0,
        ))

    return FullReport(
        total_spent=total_spent,
        number_of_expenses=number_of_expenses,
        largest_expense=largest_expense,
        highest_spending_category=highest_spending_category,
        category_summaries=category_summaries,
    )


