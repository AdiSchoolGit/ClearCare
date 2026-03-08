FROM python:3.15.0a6-slim-trixie

WORKDIR /app

COPY ../../backend/server.py server.py

COPY flask/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Moves files that live inside the parent directory into working directory
COPY . .

EXPOSE 5000

CMD ["python", "server.py"]
