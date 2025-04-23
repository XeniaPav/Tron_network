# app/routers/wallet.py
import re
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.wallet import WalletInfo
from app.schemas.wallet import WalletResponse, WalletCreate
from app.service.service_wallet import get_wallet_info

router = APIRouter()


def is_valid_tron_address(address: str) -> bool:
    """Проверка на корректный формат адреса Tron"""
    return re.match(r"^T[a-zA-Z0-9]{33}$", address) is not None


@router.post("/wallet/", response_model=WalletResponse)
async def create_wallet_request(
    wallet_request: WalletCreate, db: Session = Depends(get_db)
):
    """Роутер для вывода информации по адресу в сети трон"""
    if not is_valid_tron_address(wallet_request.address):
        raise HTTPException(status_code=400, detail="Invalid wallet address format")
    wallet_info = get_wallet_info(wallet_request.address)
    if wallet_info is None:
        raise HTTPException(
            status_code=400, detail="Invalid wallet address or wallet not found"
        )

    wallet_info_model = WalletInfo(
        address=wallet_request.address,
        bandwidth=wallet_info["bandwidth"],
        energy=wallet_info["energy"],
        balance_trx=wallet_info["balance_trx"],
    )

    db.add(wallet_info_model)
    db.commit()
    db.refresh(wallet_info_model)

    return wallet_info_model


@router.get("/wallets/")
async def read_wallet_requests(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    """Роутер выводит список последних записей из БД, включая пагинацию"""
    return db.query(WalletInfo).offset(skip).limit(limit).all()
