cat > Dockerfile << EOF
FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install fastapi streamlit uvicorn
COPY . .
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# TODO: Deploy to AWS EC2 (use free tier)
# TODO: Document deployment process for interviews