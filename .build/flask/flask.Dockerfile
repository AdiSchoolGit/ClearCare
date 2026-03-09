FROM python:3.12-slim

WORKDIR /app

COPY backend/server.py /app/server.py
COPY ./.build/flask/requirements.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

# Moves files that live inside the parent directory into working directory
COPY . .

EXPOSE 5000

CMD ["python", "server.py"]
