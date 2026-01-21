"""Transaction input form widget"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QDoubleSpinBox, QComboBox, QPushButton
)
from PyQt6.QtCore import pyqtSignal
from src.models import Transaction


class TransactionForm(QWidget):
    """Form for adding new transactions"""
    
    transaction_added = pyqtSignal(Transaction)

    def __init__(self):
        """Initialize the transaction form"""
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()

        # Description
        description_layout = QHBoxLayout()
        description_layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter transaction description...")
        description_layout.addWidget(self.description_input)
        layout.addLayout(description_layout)

        # Category
        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel("Category:"))
        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("e.g., Food, Transport, Salary...")
        category_layout.addWidget(self.category_input)
        layout.addLayout(category_layout)

        # Amount
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("Amount (€):"))
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setMinimum(0.0)
        self.amount_input.setMaximum(999999.99)
        self.amount_input.setDecimals(2)
        amount_layout.addWidget(self.amount_input)
        layout.addLayout(amount_layout)

        # Type
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Expense", "Income"])
        type_layout.addWidget(self.type_combo)
        layout.addLayout(type_layout)

        # Submit button
        self.submit_btn = QPushButton("Add Transaction")
        self.submit_btn.clicked.connect(self._on_submit)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def _on_submit(self):
        """Handle form submission"""
        description = self.description_input.text().strip()
        category = self.category_input.text().strip()
        amount = self.amount_input.value()
        transaction_type = self.type_combo.currentText().lower()

        if not description or not category or amount == 0:
            return

        transaction = Transaction(
            description=description,
            category=category,
            amount=amount,
            transaction_type=transaction_type
        )
        
        self.transaction_added.emit(transaction)
        self._clear_form()

    def _clear_form(self):
        """Clear all form inputs"""
        self.description_input.clear()
        self.category_input.clear()
        self.amount_input.setValue(0.0)
        self.type_combo.setCurrentIndex(0)
