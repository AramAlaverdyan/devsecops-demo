FROM python:3.10-alpine

# ԱՎԵԼԱՑՆՈՒՄ ԵՆՔ ԱՅՍ ՏՈՂԸ. Սա հենց build-ի պահին կներբեռնի 2026-ի բոլոր թարմ security patch-երը
RUN apk update && apk upgrade --no-cache

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY config.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
