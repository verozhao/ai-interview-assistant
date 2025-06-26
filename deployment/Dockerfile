# Dockerfile
# Placeholder for deployment Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi streamlit uvicorn
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"] 