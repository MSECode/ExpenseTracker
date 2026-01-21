"""Transaction model for expense tracking"""
from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class Transaction:
    """Represents a financial transaction (income or expense)"""
    description: str
    category: str
    amount: float
    transaction_type: Literal["income", "expense"]
    date: datetime = None
    id: int = None

    def __post_init__(self):
        """Initialize default date if not provided"""
        if self.date is None:
            self.date = datetime.now()

    def __str__(self) -> str:
        """String representation of transaction"""
        sign = "+" if self.transaction_type == "income" else "-"
        return f"{self.description} ({self.category}): {sign}€{self.amount:.2f}"

    def to_dict(self) -> dict:
        """Convert transaction to dictionary"""
        return {
            "id": self.id,
            "description": self.description,
            "category": self.category,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "date": self.date.isoformat()
        }
