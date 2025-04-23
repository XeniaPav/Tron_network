from tronpy import Tron
from tronpy.exceptions import BadAddress
import logging

logger = logging.getLogger(__name__)


def get_wallet_info(address: str):
    tron = Tron()
    try:
        account = tron.get_account(address)

        # Логируем весь ответ для отладки
        logger.info(f"Account info for {address}: {account}")

        # Проверяем наличие необходимых ключей и возвращаем значения по умолчанию, если они отсутствуют
        return {
            "bandwidth": account.get(
                "bandwidth", 0
            ),  # Возвращаем 0, если bandwidth отсутствует
            "energy": account.get("energy", 0),  # Возвращаем 0, если energy отсутствует
            "balance_trx": account.get("balance", 0)
            / 1_000_000,  # Преобразуем из SUN в TRX
        }
    except BadAddress as e:
        logger.error(f"Bad address provided: {address}. Error: {e}")
        return None
    except Exception as e:
        logger.error(
            f"An error occurred while fetching wallet info for address {address}: {e}"
        )
        return None
