FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app


RUN uv sync --frozen --no-cache
EXPOSE 8000
CMD ["/app/.venv/bin/uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
