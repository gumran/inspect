FROM python:3.12-slim

WORKDIR /app

COPY game.py fen.txt /app/

RUN apt-get update && \
    apt-get install -y stockfish && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir chess