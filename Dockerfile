# Անցնում ենք գերանվտանգ Alpine Linux-ին
FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY config.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
