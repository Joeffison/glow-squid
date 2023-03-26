FROM python:3.11-slim

WORKDIR /app

# skip .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# make sure console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .

COPY src/ src/

RUN poetry install

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
