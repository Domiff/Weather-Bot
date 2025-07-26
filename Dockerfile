FROM python:3.12-slim

ENV POETRY_VERSION=1.8.0 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 6000

CMD ["python", "main.py"]
