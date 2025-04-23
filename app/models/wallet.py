from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base
from sqlalchemy.sql import func


class WalletInfo(Base):
    """Модель кошелька"""

    __tablename__ = "wallet_info"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    bandwidth = Column(Float)
    energy = Column(Float)
    balance_trx = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
