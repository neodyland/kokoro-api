FROM ghcr.io/astral-sh/uv:debian
COPY . /work
WORKDIR /work
RUN uv sync --no-dev --frozen
RUN ./scripts/install.sh
CMD ["uv", "run" ,"main.py"]