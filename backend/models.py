from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    id: int
    category: str
    amount: float
    timestamp: datetime

@dataclass
class Visit:
    id: int
    action: str
    timestamp: datetime
