FROM ghcr.io/astral-sh/uv:debian
COPY . /work
WORKDIR /work
RUN uv install
RUN ./scripts/install.sh
CMD ["uv", "run" ,"main.py"]