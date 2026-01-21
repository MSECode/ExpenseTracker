"""Chart widgets for data visualization"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from typing import List, Dict
from collections import defaultdict


class PieChart(QWidget):
    """Pie chart widget for category breakdown"""

    def __init__(self, title: str = "Breakdown"):
        """Initialize pie chart"""
        super().__init__()
        self.title = title
        self._setup_ui()

    def _setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()
        
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, data: Dict[str, float]):
        """Plot pie chart with transaction data"""
        if not data:
            self.figure.clear()
            self.canvas.draw()
            return

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        ax.pie(
            data.values(),
            labels=data.keys(),
            autopct='%1.1f%%',
            startangle=90
        )
        ax.set_title(self.title, fontsize=12, fontweight='bold')
        
        self.figure.tight_layout()
        self.canvas.draw()

    def update_data(self, transactions: List):
        """Update chart with transaction data"""
        data = defaultdict(float)
        
        for transaction in transactions:
            data[transaction.category] += transaction.amount
        
        self.plot(dict(data))


class BarChart(QWidget):
    """Bar chart widget for expense/income comparison"""

    def __init__(self, title: str = "Summary"):
        """Initialize bar chart"""
        super().__init__()
        self.title = title
        self._setup_ui()

    def _setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()
        
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, expenses: float, incomes: float):
        """Plot bar chart with expenses and incomes"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        categories = ['Expenses', 'Incomes']
        values = [expenses, incomes]
        colors = ['#dc3545', '#28a745']
        
        ax.bar(categories, values, color=colors, alpha=0.7, edgecolor='black')
        ax.set_ylabel('Amount (€)', fontsize=10)
        ax.set_title(self.title, fontsize=12, fontweight='bold')
        
        # Add value labels on bars
        for i, (category, value) in enumerate(zip(categories, values)):
            ax.text(i, value, f'€{value:.2f}', ha='center', va='bottom')
        
        self.figure.tight_layout()
        self.canvas.draw()

    def update_data(self, expenses: float, incomes: float):
        """Update chart with new data"""
        self.plot(expenses, incomes)
