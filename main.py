import os
from fastapi import FastAPI, Request
from app.database import init_db
from app.routers.wallet import router
from app.logging_config import setup_logging
import logging

setup_logging()  # Настройка логирования перед созданием FastAPI приложения
logger = logging.getLogger(__name__)

app = FastAPI(debug=True)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


# Подключение роутеров к приложению
app.include_router(router)

if __name__ == "__main__":
    try:
        # Инициализация базы данных
        init_db()
        print("База данных успешно инициализирована.")

        # Запуск приложения (если нужно)
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=8000)

    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

