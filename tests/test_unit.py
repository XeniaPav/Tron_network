import pytest
from app.models.wallet import WalletInfo
from app.database import SessionLocal


@pytest.fixture(scope="module")
def test_db():
    db = SessionLocal()

    yield db

    db.close()


def test_create_wallet_request(test_db):
    new_request = WalletInfo(
        address="TXYZ...", bandwidth=1000.0, energy=2000.0, balance_trx=10.0
    )
    test_db.add(new_request)
    test_db.commit()
    assert new_request.id is not None


def test_get_wallet_requests(test_db):
    requests = test_db.query(WalletInfo).all()
    assert len(requests) > 0  # Проверяем что есть хотя бы одна запись.
