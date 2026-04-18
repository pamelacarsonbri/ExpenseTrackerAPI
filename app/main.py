from fastapi import FastAPI
from app.database import engine, Base
from app.routes import expenses_router, budgets_router, report_router

# Create all database tables on startup (if they don't exist yet)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Expense Tracker API",
    description=(
        "A REST API for tracking personal expenses and monthly budgets. "
        "Built with FastAPI, SQLAlchemy, and MySQL.\n\n"
        "**Categories:** Food, Transport, Entertainment, Utilities, Health, Other"
    ),
    version="1.0.0",
)

# Register all routers
app.include_router(expenses_router)
app.include_router(budgets_router)
app.include_router(report_router)

@app.get("/", tags=["Health"])
def root():
    """Health check — confirms the API is running."""
    return {"message": "Expense Tracker API is running. Visit http://127.0.0.1:8000/docs directly in your browser to explore all endpoints."}

