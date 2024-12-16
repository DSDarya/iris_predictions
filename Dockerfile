FROM python:3.9

COPY requirements.txt .env ./

RUN pip install --no-cache-dir -r requirements.txt

COPY project ./app

WORKDIR /app

EXPOSE ${APP_PORT}

VOLUME app

CMD uvicorn app.iris_app:app --reload --port ${APP_PORT} --host 0.0.0.0
