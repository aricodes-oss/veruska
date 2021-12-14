FROM python:latest

RUN apt-get update
RUN apt-get install -y ffmpeg libffi-dev libnacl-dev python3-dev

RUN mkdir /code
WORKDIR /code
RUN mkdir veruska

RUN pip install --upgrade poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-root

COPY veruska veruska

RUN poetry install

CMD ["poetry", "run", "veruska"]
