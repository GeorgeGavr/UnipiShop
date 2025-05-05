# Base image
FROM python:3.11-slim

# Δημιουργία φακέλου για την εφαρμογή
WORKDIR /app

# Αντιγραφή των dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Αντιγραφή όλων των αρχείων του project στον container
COPY . .

# Ορίζουμε την εντολή για να ξεκινήσει το Flask app
CMD ["python", "api.py"]
