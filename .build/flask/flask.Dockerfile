FROM python:3.15.0a6-slim-trixie

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Moves files that live inside the parent directory into working directory
COPY . .

EXPOSE 5000

# Missing second arg e.g. webserver.py or app.py
CMD ["python" ]
