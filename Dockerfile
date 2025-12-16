FROM python:3.14-alpine

WORKDIR /app/simple_crm

RUN apk add --no-cache \
    build-base \
    python3-dev \
    libpq \
    libpq-dev \
    postgresql-dev \
    musl-dev \
    linux-headers

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY pyproject.toml ./
RUN pip install --no-cache-dir .

COPY . .
