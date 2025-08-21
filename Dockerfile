FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# deps (ok if requirements.txt is empty)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true

# app code
COPY . .

# run the script (not a server)
CMD ["python", "app.py"]

