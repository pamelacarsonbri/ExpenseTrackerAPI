# 💸 Personal Expense Tracker API

> A backend system for tracking personal expenses and monthly budgets — built with FastAPI, SQLAlchemy, and MySQL.

---

## The Problem

Managing money is hard when you have no visibility into where it goes. This API lets you log daily expenses by category, set monthly budgets, and generate a full spending report — so you always know where you stand.

---

## What It Does

- Log expenses with a date, category, description, and amount
- Set and update monthly budgets per category
- View all expenses or filter by category
- Get a full spending report: total spent, largest expense, top category, and a budget vs. spent breakdown per category
- Returns proper JSON responses with correct HTTP status codes
- Input is validated — bad data is rejected with a clear error message
- Budget warnings when spending exceeds any category limit

---

## Live Links

| | |
|---|---|
| **Frontend** | [https://pamelacarsonbri.github.io/expense-tracker-frontend/](https://pamelacarsonbri.github.io/expense-tracker-frontend/) |
| **API** | [https://expensetrackerapi-1-x5ss.onrender.com](https://expensetrackerapi-1-x5ss.onrender.com) |
| **API Docs** | [https://expensetrackerapi-1-x5ss.onrender.com/docs](https://expensetrackerapi-1-x5ss.onrender.com/docs) |
| **GitHub (Frontend)** | [https://github.com/pamelacarsonbri/expense-tracker-frontend](https://github.com/pamelacarsonbri/expense-tracker-frontend) |
| **GitHub (Backend)** | [https://github.com/pamelacarsonbri/ExpenseTrackerAPI](https://github.com/pamelacarsonbri/ExpenseTrackerAPI) |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Programming language |
| FastAPI | Web framework for building the REST API |
| SQLAlchemy | ORM for database interaction |
| MySQL (Aiven) | Cloud-hosted relational database |
| PyMySQL | MySQL driver for SQLAlchemy |
| Pydantic | Request/response data validation |
| python-dotenv | Load environment variables from `.env` |
| Uvicorn | ASGI server to run the app |
| Render | Cloud hosting for the API |
| GitHub Pages | Hosting for the frontend |

---

## API Endpoints

| Method | Path | Description |
|--------|----------|-------------|
| GET |     `/`     | HTML landing page with live links |
| **Expenses** | | |
| POST | `/expenses/` | Log a new expense |
| GET | `/expenses/` | Get all expenses |
| GET | `/expenses/{id}` | Get one expense by ID |
| GET | `/expenses/category/{category}` | Get all expenses in a category |
| DELETE | `/expenses/{id}` | Delete an expense |
| **Budgets** | | |
| POST | `/budgets/` | Set or update a category budget |
| GET | `/budgets/` | Get all budgets |
| GET | `/budgets/{category}` | Get budget for one category |
| **Report** | | |
| GET | `/report/` | Get full spending report |

**Valid categories:** `Food`, `Transport`, `Entertainment`, `Utilities`, `Health`, `Other`

---

## Example Requests & Responses

### Log an Expense

**Request:**
```
POST /expenses/
Content-Type: application/json

{
  "category": "Food",
  "description": "Lunch at KFC",
  "amount": 45.50,
  "date": "2026-04-13"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "date": "2026-04-13",
  "category": "Food",
  "description": "Lunch at KFC",
  "amount": 45.5
}
```

---

### Set a Budget

**Request:**
```
POST /budgets/
Content-Type: application/json

{
  "category": "Food",
  "amount": 200.00
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "category": "Food",
  "amount": 200.0
}
```

---

### Get Full Report

**Request:**
```
GET /report/
```

**Response (200 OK):**
```json
{
  "total_spent": 145.5,
  "number_of_expenses": 2,
  "largest_expense": {
    "id": 2,
    "date": "2026-04-13",
    "category": "Health",
    "description": "Pharmacy",
    "amount": 100.0
  },
  "highest_spending_category": "Health",
  "category_summaries": [
    {
      "category": "Food",
      "budget": 200.0,
      "spent": 45.5,
      "remaining": 154.5,
      "over_budget": false
    }
  ]
}
```

---

### Error Example — Item Not Found

**Request:**
```
GET /expenses/999
```

**Response (404 Not Found):**
```json
{
  "detail": "Expense with id 999 not found."
}
```

---

## How to Test It

### Option A — Use the Frontend (Easiest)

Visit the live frontend and use the dashboard to log expenses, set budgets, and view your spending report — no technical knowledge needed:

**[https://pamelacarsonbri.github.io/expense-tracker-frontend](https://pamelacarsonbri.github.io/expense-tracker-frontend)**

![Frontend Screenshot](Frontend_Screenshot.jpeg)
---

### Option B — Use the /docs Page (Swagger UI)

Visit the interactive API docs and test every endpoint directly in the browser:

**[https://expensetrackerapi-1-x5ss.onrender.com/docs](https://expensetrackerapi-1-x5ss.onrender.com/docs)**

Click any endpoint → click **Try it out** → fill in the form → click **Execute** to see the live response.

![API Docs Screenshot](API_Docs_Screenshot.jpeg)

---

### Option C — Use Postman

1. Download Postman for free at [https://www.postman.com/downloads](https://www.postman.com/downloads)
2. Clone this repository from GitHub
3. Open Postman and click **Import**
4. Select the file `postman_collection.json` from the project folder
5. All endpoints will appear ready to use — click any request and hit **Send**

> All requests are pre-filled with example data so you can test every endpoint with one click.

---

## Author

**Pamela Carson** — Tech4Girls Cohort 4
[github.com/pamelacarsonbri](https://github.com/pamelacarsonbri)
