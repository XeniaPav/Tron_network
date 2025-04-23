from pydantic import BaseModel


class WalletCreate(BaseModel):
    """" Схема создания кошелька """
    address: str


class WalletResponse(BaseModel):
    """ Схема для получения информации о конкретном кошельке """
    id: int
    address: str
    bandwidth: float
    energy: float
    balance_trx: float

    class Config:
        from_attributes = True


class WalletListResponse(BaseModel):
    """ Схема для получения списка кошельков """
    wallets: list[WalletResponse]
