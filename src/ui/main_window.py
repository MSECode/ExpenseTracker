"""Main application window"""
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QTabWidget, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from src.models import Database, Transaction
from src.ui.widgets.transaction_form import TransactionForm
from src.ui.widgets.transaction_list import TransactionList
from src.ui.widgets.charts import PieChart, BarChart


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self):
        """Initialize main window"""
        super().__init__()
        self.db = Database()
        self._setup_ui()
        self._load_data()

    def _setup_ui(self):
        """Setup the user interface"""
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 1200, 800)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()

        # Header with balance
        header_layout = QHBoxLayout()
        balance_label = QLabel("Your Balance:")
        balance_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        header_layout.addWidget(balance_label)
        
        self.balance_display = QLabel("€0.00")
        self.balance_display.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.balance_display.setStyleSheet("color: #28a745;")
        header_layout.addWidget(self.balance_display)
        header_layout.addStretch()
        
        main_layout.addLayout(header_layout)

        # Tabs for different sections
        self.tabs = QTabWidget()

        # Transaction Tab
        transaction_tab = QWidget()
        transaction_layout = QVBoxLayout()
        
        self.transaction_form = TransactionForm()
        self.transaction_form.transaction_added.connect(self._add_transaction)
        transaction_layout.addWidget(self.transaction_form)
        
        transaction_tab.setLayout(transaction_layout)
        self.tabs.addTab(transaction_tab, "Add Transaction")

        # Overview Tab
        overview_tab = QWidget()
        overview_layout = QHBoxLayout()
        
        charts_container = QVBoxLayout()
        self.bar_chart = BarChart("Expenses vs Incomes")
        charts_container.addWidget(self.bar_chart)
        overview_layout.addLayout(charts_container)
        
        overview_tab.setLayout(overview_layout)
        self.tabs.addTab(overview_tab, "Overview")

        # Expenses Tab
        expenses_tab = QWidget()
        expenses_layout = QHBoxLayout()
        
        expenses_list_layout = QVBoxLayout()
        expenses_list_layout.addWidget(QLabel("Recent Expenses:"))
        self.expenses_list = TransactionList()
        expenses_list_layout.addWidget(self.expenses_list)
        expenses_layout.addLayout(expenses_list_layout)
        
        expenses_chart_layout = QVBoxLayout()
        expenses_chart_layout.addWidget(QLabel("Expenses by Category:"))
        self.expenses_chart = PieChart("Expenses Breakdown")
        expenses_chart_layout.addWidget(self.expenses_chart)
        expenses_layout.addLayout(expenses_chart_layout)
        
        expenses_info_layout = QVBoxLayout()
        expenses_info_layout.addWidget(QLabel("Total Expenses:"))
        self.total_expenses_label = QLabel("€0.00")
        self.total_expenses_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.total_expenses_label.setStyleSheet("color: #dc3545;")
        expenses_info_layout.addWidget(self.total_expenses_label)
        expenses_info_layout.addStretch()
        expenses_layout.addLayout(expenses_info_layout)
        
        expenses_tab.setLayout(expenses_layout)
        self.tabs.addTab(expenses_tab, "Expenses")

        # Incomes Tab
        incomes_tab = QWidget()
        incomes_layout = QHBoxLayout()
        
        incomes_list_layout = QVBoxLayout()
        incomes_list_layout.addWidget(QLabel("Recent Incomes:"))
        self.incomes_list = TransactionList()
        incomes_list_layout.addWidget(self.incomes_list)
        incomes_layout.addLayout(incomes_list_layout)
        
        incomes_chart_layout = QVBoxLayout()
        incomes_chart_layout.addWidget(QLabel("Incomes by Category:"))
        self.incomes_chart = PieChart("Incomes Breakdown")
        incomes_chart_layout.addWidget(self.incomes_chart)
        incomes_layout.addLayout(incomes_chart_layout)
        
        incomes_info_layout = QVBoxLayout()
        incomes_info_layout.addWidget(QLabel("Total Incomes:"))
        self.total_incomes_label = QLabel("€0.00")
        self.total_incomes_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.total_incomes_label.setStyleSheet("color: #28a745;")
        incomes_info_layout.addWidget(self.total_incomes_label)
        incomes_info_layout.addStretch()
        incomes_layout.addLayout(incomes_info_layout)
        
        incomes_tab.setLayout(incomes_layout)
        self.tabs.addTab(incomes_tab, "Incomes")

        main_layout.addWidget(self.tabs)
        central_widget.setLayout(main_layout)

    def _load_data(self):
        """Load and display all data from database"""
        self._update_display()

    def _update_display(self):
        """Refresh all displays with current data"""
        # Get data from database
        all_transactions = self.db.get_all_transactions()
        expenses = self.db.get_expenses()
        incomes = self.db.get_incomes()
        balance = self.db.get_balance()

        # Update balance
        balance_color = "#28a745" if balance >= 0 else "#dc3545"
        self.balance_display.setText(f"€{balance:.2f}")
        self.balance_display.setStyleSheet(f"color: {balance_color};")

        # Update lists
        self.expenses_list.update_transactions(expenses)
        self.incomes_list.update_transactions(incomes)

        # Update charts
        total_expenses = self.db.get_total_expenses()
        total_incomes = self.db.get_total_incomes()
        
        self.bar_chart.update_data(total_expenses, total_incomes)
        self.expenses_chart.update_data(expenses)
        self.incomes_chart.update_data(incomes)

        # Update totals
        self.total_expenses_label.setText(f"€{total_expenses:.2f}")
        self.total_incomes_label.setText(f"€{total_incomes:.2f}")

    def _add_transaction(self, transaction: Transaction):
        """Handle new transaction"""
        try:
            self.db.add_transaction(transaction)
            self._update_display()
            QMessageBox.information(
                self,
                "Success",
                f"Transaction added: {transaction.description}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add transaction: {str(e)}")

    def closeEvent(self, event):
        """Handle application close"""
        reply = QMessageBox.question(
            self,
            "Exit Application",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
