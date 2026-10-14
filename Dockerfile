FROM ghcr.io/astral-sh/uv:python3.14-alpine AS Builder
COPY pyproject.toml uv.lock /app/
WORKDIR /app
RUN uv sync --frozen --no-dev --no-install-project
COPY api/ /app/api/
RUN uv sync --frozen --no-dev

FROM python:3.14-alpine
WORKDIR /app
RUN adduser --system --home /home/nonroot nonroot && chown -R nonroot /app/
COPY --from=Builder /app/.venv/ /app/.venv/
COPY --from=Builder /app/api/ /app/api/
ENV PATH="/app/.venv/bin:$PATH"
USER nonroot
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]