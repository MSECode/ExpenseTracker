"""Database management for expense tracker"""
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import List
from .transaction import Transaction


class Database:
    """Handles all database operations for transactions"""

    def __init__(self, db_path: str = "data/transactions.db"):
        """Initialize database connection"""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize_db()

    def _initialize_db(self):
        """Create tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('income', 'expense')),
                    date TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_transaction(self, transaction: Transaction) -> int:
        """Add a new transaction to database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO transactions 
                (description, category, amount, transaction_type, date)
                VALUES (?, ?, ?, ?, ?)
            """, (
                transaction.description,
                transaction.category,
                transaction.amount,
                transaction.transaction_type,
                transaction.date.isoformat()
            ))
            conn.commit()
            return cursor.lastrowid

    def get_all_transactions(self) -> List[Transaction]:
        """Retrieve all transactions from database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, description, category, amount, transaction_type, date
                FROM transactions ORDER BY date DESC
            """)
            transactions = []
            for row in cursor.fetchall():
                transaction = Transaction(
                    id=row[0],
                    description=row[1],
                    category=row[2],
                    amount=row[3],
                    transaction_type=row[4],
                    date=datetime.fromisoformat(row[5])
                )
                transactions.append(transaction)
            return transactions

    def get_expenses(self) -> List[Transaction]:
        """Get all expenses"""
        return [t for t in self.get_all_transactions() if t.transaction_type == "expense"]

    def get_incomes(self) -> List[Transaction]:
        """Get all incomes"""
        return [t for t in self.get_all_transactions() if t.transaction_type == "income"]

    def delete_transaction(self, transaction_id: int) -> bool:
        """Delete a transaction by id"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_balance(self) -> float:
        """Calculate current balance (incomes - expenses)"""
        transactions = self.get_all_transactions()
        balance = sum(t.amount for t in transactions if t.transaction_type == "income")
        balance -= sum(t.amount for t in transactions if t.transaction_type == "expense")
        return balance

    def get_total_expenses(self) -> float:
        """Get total amount spent on expenses"""
        expenses = self.get_expenses()
        return sum(t.amount for t in expenses)

    def get_total_incomes(self) -> float:
        """Get total amount of incomes"""
        incomes = self.get_incomes()
        return sum(t.amount for t in incomes)
