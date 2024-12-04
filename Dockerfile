FROM python:3.11.10-alpine3.20

COPY pyproject.toml poetry.lock main.py ./

ADD api api

RUN pip install poetry && poetry install --no-root --no-dev

EXPOSE 8000

RUN poetry install

CMD ["poetry", "run", "app"]

