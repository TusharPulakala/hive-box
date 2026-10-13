FROM ghcr.io/astral-sh/uv:python3.14-alpine AS Builder
COPY . /app
WORKDIR /app
RUN uv sync --frozen --no-dev
CMD ["uv", "run", "fastapi", "dev"]