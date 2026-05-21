# Օգտագործում ենք Python-ի պաշտոնական բազան
FROM python:3.10-slim

# Սահմանում ենք աշխատանքային պանակը կոնտեյների ներսում
WORKDIR /app

# Պատճենում ենք մեր ֆայլերը կոնտեյների մեջ
COPY requirements.txt .
COPY app.py .
COPY config.py .

# Տեղադրում ենք Python-ի library-ները
RUN pip install --no-cache-dir -r requirements.txt

# Հրաման, որով աշխատելու է մեր հավելվածը
CMD ["python", "app.py"]
