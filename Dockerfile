FROM python:3.9-slim

RUN apt update && apt install --assume-yes curl

ARG APP_DIR=/var/app

ENV PATH=/root/.poetry/bin:${PATH} \
    PIP_NO_CACHE_DIR=off \
    POETRY_VIRTUALENVS_CREATE=false

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR $APP_DIR

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY main.py .
COPY otodom_url.txt .

RUN mkdir -p $APP_DIR/data

VOLUME v

CMD ["/bin/bash"]
