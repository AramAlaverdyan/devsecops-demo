FROM python:3.10-alpine

RUN apk update && apk upgrade --no-cache

WORKDIR /app

COPY requirements.txt .

# ԱՎԵԼԱՑՆՈՒՄ ԵՆՔ ԱՅՍ ՏՈՂԸ. Թարմացնում ենք Python-ի հիմնական համակարգային գործիքները
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY app.py .
COPY config.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
