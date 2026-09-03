FROM python:3.13-slim

WORKDIR /app

COPY requirment.txt .

RUN pip install --no-cache-dir -r requirment.txt

COPY . .

CMD ["python", "extract.py"]