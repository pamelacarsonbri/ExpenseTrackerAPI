from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers
app.include_router(expenses_router)
app.include_router(budgets_router)
app.include_router(report_router)


@app.get("/", response_class=HTMLResponse, tags=["Health"])
def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Expense Tracker API</title>
      <style>
        body { font-family: sans-serif; max-width: 600px; margin: 80px auto; padding: 0 24px; color: #0f1923; }
        h1 { font-size: 24px; margin-bottom: 8px; }
        p { color: #6b7280; margin-bottom: 32px; }
        .card { background: #f7f9fc; border: 1px solid #e5e9f0; border-radius: 10px; padding: 24px; margin-bottom: 16px; }
        .label { font-size: 12px; font-weight: 600; color: #6b7280; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }
        a { color: #1a6ef5; text-decoration: none; font-size: 15px; font-weight: 500; }
        a:hover { text-decoration: underline; }
        .dot { display: inline-block; width: 8px; height: 8px; background: #10b981; border-radius: 50%; margin-right: 8px; }
        .status { font-size: 14px; color: #10b981; font-weight: 500; }
      </style>
    </head>
    <body>
      <h1>Personal Expense Tracker API</h1>
      <p>Built with FastAPI, SQLAlchemy and MySQL · Tech4Girls Cohort 4</p>

      <div class="card">
        <div class="label">Status</div>
        <span class="dot"></span>
        <span class="status">Online and running</span>
      </div>

      <div class="card">
        <div class="label">Frontend</div>
        <a href="https://pamelacarsonbri.github.io/expense-tracker-frontend" target="_blank">
          https://pamelacarsonbri.github.io/expense-tracker-frontend/
        </a>
      </div>

      <div class="card">
        <div class="label">API Docs (Swagger UI)</div>
        <a href="/docs" target="_blank">
          View all endpoints →
        </a>
      </div>

      <div class="card">
        <div class="label">GitHub</div>
        <a href="https://expensetrackerapi-1-x5ss.onrender.com/docs" target="_blank">
          https://expensetrackerapi-1-x5ss.onrender.com/docs
        </a>
      </div>
    </body>
    </html>
    """