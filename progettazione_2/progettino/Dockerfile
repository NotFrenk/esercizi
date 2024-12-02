FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY query.py .
EXPOSE 5001
CMD ["python", "query.py"]