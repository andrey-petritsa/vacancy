FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app
COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

CMD ["python", "vacancy/main/main.py", "run"]