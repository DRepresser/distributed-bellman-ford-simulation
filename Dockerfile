FROM python:3.9-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir flask

CMD ["python", "node.py"]