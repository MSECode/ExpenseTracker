# Expense Tracker

A modern desktop application for tracking personal expenses and income.

## Overview

This application helps you manage your finances by:
- Adding and tracking transactions (expenses and income)
- Categorizing transactions for better organization
- Visualizing spending patterns with charts
- Calculating your current balance
- Maintaining a persistent local database

## Architecture

### Technology Stack
- **PyQt6**: Cross-platform desktop GUI framework
- **SQLite**: Local persistent database
- **Matplotlib**: Data visualization and charting
- **Python 3.10+**: Core language

### Project Structure
```
expense-tracker/
├── main.py                 # Application entry point
├── src/
│   ├── models/            # Data models
│   │   ├── transaction.py # Transaction dataclass
│   │   └── database.py    # Database operations
│   ├── ui/                # User interface
│   │   ├── main_window.py # Main application window
│   │   └── widgets/       # Reusable UI components
│   │       ├── transaction_form.py
│   │       ├── transaction_list.py
│   │       └── charts.py
│   └── utils/             # Utility functions
├── data/                  # Application data (created at runtime)
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation & Setup

### 1. Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

## Features

### Current Features (MVP - Minimum Viable Product)
- ✅ Add transactions with description, category, and amount
- ✅ Classify transactions as income or expense
- ✅ View transaction history
- ✅ Calculate current balance
- ✅ Visualize expenses and incomes with charts
- ✅ Persistent data storage in SQLite
- ✅ Responsive tabbed interface

## Usage

### Adding a Transaction
1. Open the app and go to "Add Transaction" tab
2. Fill in:
   - **Description**: What was the transaction for?
   - **Category**: Classify it (e.g., Food, Transport, Salary)
   - **Amount**: How much?
   - **Type**: Income or Expense?
3. Click "Add Transaction"

### Viewing Data
- **Overview Tab**: See overall balance and expense/income comparison
- **Expenses Tab**: View all expenses and breakdown by category
- **Incomes Tab**: View all incomes and breakdown by category

## Database

The app uses SQLite for persistent storage. The database file is located at:
```
data/transactions.db
```

## Planned Features & Improvement Paths

### 🔴 Phase 2: Core Enhancements (Recommended Next Steps)
1. **Transaction Management**
   - [ ] Edit existing transactions
   - [ ] Delete transactions with confirmation
   - [ ] Search and filter transactions
   - [ ] Date range filtering

2. **UI Improvements**
   - [ ] Dark/Light theme toggle
   - [ ] Customizable categories
   - [ ] Better date selection UI

3. **Data Features**
   - [ ] Export to CSV
   - [ ] Import from CSV

### 🟡 Phase 3: Advanced Features
1. **Multi-Account Support**
   - [ ] Multiple account types (savings, checking, etc.)
   - [ ] Account switching
   - [ ] Transfer between accounts

2. **Budgeting**
   - [ ] Set budget limits per category
   - [ ] Budget alerts
   - [ ] Recurring transaction templates

3. **Advanced Analytics**
   - [ ] Monthly trend analysis
   - [ ] Budget vs actual spending
   - [ ] Year-over-year comparison
   - [ ] Category-wise reports

### 🟢 Phase 4: Premium Features
1. **Smart Features**
   - [ ] Spending patterns analysis
   - [ ] Predictive budgeting
   - [ ] Anomaly detection
   - [ ] Auto-categorization

2. **Data Management**
   - [ ] Database backup/restore
   - [ ] Cloud sync (optional)
   - [ ] Custom report builder
   - [ ] Scheduled reports

## Suggested Development Path

I recommend tackling improvements in this order:

1. **Week 1**: Add delete and edit functionality (Phase 2)
2. **Week 2**: Add search/filter and date-based filtering (Phase 2)
3. **Week 3**: Improve UI with themes and better date pickers (Phase 2)
4. **Week 4**: Add CSV export/import (Phase 2)
5. **Month 2**: Budget tracking (Phase 3)
6. **Month 3+**: Multi-account and advanced analytics (Phase 3-4)

## Development Notes

### Code Organization
- **models/**: Data structures and database operations
- **ui/**: All GUI-related code
- **ui/widgets/**: Reusable UI components
- **utils/**: Helper functions and constants

### Database Schema
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    transaction_type TEXT NOT NULL,
    date TEXT NOT NULL
)
```

## Troubleshooting

### Database Issues
If you encounter database errors, delete `data/transactions.db` and restart the app.

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Next Immediate Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python main.py`
3. Add some test transactions
4. Choose a feature from Phase 2 to implement next
5. Let me know which path interests you most!
