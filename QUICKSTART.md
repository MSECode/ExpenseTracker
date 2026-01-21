# 🚀 Quick Start Guide

## 1️⃣ Installation (5 minutes)

### Linux/macOS
```bash
cd /home/jlosi/Workspace/AccountingWebApp
bash setup.sh
python main.py
```

### Windows
```bash
cd AccountingWebApp
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Or Manual (All Platforms)
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

---

## 2️⃣ First Steps

### Step 1: Add a Transaction
1. Click on "Add Transaction" tab
2. Fill in the fields:
   - **Description**: "Coffee at Cafe"
   - **Category**: "Food"
   - **Amount**: 5.50
   - **Type**: Expense
3. Click "Add Transaction"

### Step 2: View Your Data
- **Overview Tab**: See total income vs expenses
- **Expenses Tab**: See all expenses and breakdown by category
- **Incomes Tab**: See all incomes and breakdown by category

### Step 3: Try More Transactions
```
Test Data to Add:
- Salary: €2000 (Income)
- Rent: €1000 (Expense)
- Groceries: €150 (Expense)
- Freelance Work: €300 (Income)
- Gas: €50 (Expense)
```

---

## 3️⃣ Understanding the Interface

```
┌─────────────────────────────────────────┐
│ Expense Tracker     Your Balance: €1100  │  ← Header
├─────────────────────────────────────────┤
│  [Add Transaction] [Overview] [Expenses] [Incomes]  │  ← Tabs
├─────────────────────────────────────────┤
│                                           │
│        Tab Content Area                   │
│        (Changes based on selected tab)    │
│                                           │
└─────────────────────────────────────────┘
```

---

## 4️⃣ File Locations

```
Important Files:
├── main.py              ← Run this to start app
├── requirements.txt     ← Dependencies
├── data/transactions.db ← Your data (created automatically)
├── README.md            ← Full documentation
├── MIGRATION_SUMMARY.md ← This document
└── src/                 ← Application code
```

---

## 5️⃣ Troubleshooting

| Problem | Solution |
|---------|----------|
| "No module named PyQt6" | Run: `pip install -r requirements.txt` |
| App won't start | Make sure virtual environment is activated |
| Charts don't show | Add at least one transaction first |
| Database errors | Delete `data/transactions.db` and restart |

---

## 6️⃣ What's Next?

After testing the basic app, consider:

### Easy (1-2 hours)
- [ ] Add "Edit Transaction" button
- [ ] Add "Delete Transaction" button
- [ ] Add search bar

### Medium (2-4 hours)
- [ ] Add date picker widget
- [ ] Add export to CSV
- [ ] Add category customization

### Advanced (4+ hours)
- [ ] Budget tracking system
- [ ] Monthly reports
- [ ] Spending predictions

---

## 7️⃣ Useful Commands

```bash
# Activate environment
source venv/bin/activate

# Install new package
pip install package_name

# Run app
python main.py

# Deactivate environment
deactivate

# View installed packages
pip list
```

---

## 8️⃣ Project Structure Quick Reference

```
src/
├── models/
│   ├── transaction.py   ← Data structure
│   └── database.py      ← SQLite operations
├── ui/
│   ├── main_window.py   ← Main application
│   └── widgets/         ← UI components
│       ├── transaction_form.py
│       ├── transaction_list.py
│       └── charts.py
└── utils/               ← Helper functions
```

---

## 9️⃣ Key Features Available Now

✅ Add transactions  
✅ View balance  
✅ See expenses/incomes breakdown  
✅ Visualize data with charts  
✅ Persistent database storage  
✅ Multi-tab interface  

---

## 🔟 Need Help?

1. **Questions about code?** Check files in `src/` - they have comments
2. **Need new features?** See MIGRATION_SUMMARY.md for suggestions
3. **Database issues?** Delete `data/transactions.db` and restart
4. **Installation issues?** Ensure Python 3.10+ and pip is updated

---

**Ready to go? Run:** `python main.py` 🎯
