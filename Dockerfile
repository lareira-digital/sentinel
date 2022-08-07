FROM python:3.10-alpine
LABEL maintainer="Oscar Carballal Prego <oscar@lareira.digital>"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_PATH="/app/.venv" \
    POETRY_VIRTUALENVS_IN_PROJECT=true 

RUN apk add --no-cache \
        curl \
        gcc \
        g++ \
        libressl-dev \
        musl-dev \
        libffi-dev \
    && curl -sSL https://install.python-poetry.org | python3 - 

RUN mkdir -p /app
ENV PATH="$POETRY_HOME/bin:/app:$PATH"
WORKDIR /app
COPY . /app/
RUN chmod +x /app/startup_script.sh
RUN poetry install --no-dev --no-root --no-interaction

# Cleanup
RUN apk del \
        curl \
        gcc \
        g++ \
        libressl-dev \
        musl-dev \
        libffi-dev
RUN rm -rf /app/.git/

EXPOSE 80

ENTRYPOINT ["./startup_script.sh"]