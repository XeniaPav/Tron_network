from sqlalchemy.orm import Session
from app.models.wallet import WalletInfo


def create_wallet(
    db: Session, address: str, bandwidth: float, energy: float, balance_trx: float
):
    """ Создание кошелька """
    db_wallet = WalletInfo(
        address=address, bandwidth=bandwidth, energy=energy, balance_trx=balance_trx
    )
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet


def get_wallets(db: Session, skip: int = 0, limit: int = 10):
    """ Получение списка кошельков """
    return db.query(WalletInfo).offset(skip).limit(limit).all()
