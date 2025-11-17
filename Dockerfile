FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Run FastAPI using its built-in runner (not uvicorn command)
CMD ["python", "-m", "fastapi", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]
