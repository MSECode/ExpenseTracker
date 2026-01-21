"""Transaction list display widget"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget, 
    QListWidgetItem, QPushButton
)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QColor
from src.models import Transaction


class TransactionList(QWidget):
    """Display list of transactions"""
    
    transaction_deleted = pyqtSignal(int)

    def __init__(self):
        """Initialize transaction list"""
        super().__init__()
        self._setup_ui()
        self.transactions = {}

    def _setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()

        title = QLabel("Recent Transactions")
        title.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(title)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_transaction(self, transaction: Transaction):
        """Add a transaction to the list"""
        item = QListWidgetItem()
        
        # Color code: green for income, red for expense
        if transaction.transaction_type == "income":
            color = QColor("#28a745")
            text = f"+ €{transaction.amount:.2f}"
        else:
            color = QColor("#dc3545")
            text = f"- €{transaction.amount:.2f}"
        
        display_text = f"{transaction.description} ({transaction.category}) {text}"
        item.setText(display_text)
        item.setForeground(color)
        
        self.list_widget.insertItem(0, item)
        self.transactions[id(item)] = transaction.id

    def update_transactions(self, transactions: list):
        """Replace all transactions in the list"""
        self.list_widget.clear()
        self.transactions.clear()
        
        for transaction in transactions:
            self.add_transaction(transaction)

    def clear(self):
        """Clear all transactions from the list"""
        self.list_widget.clear()
        self.transactions.clear()
