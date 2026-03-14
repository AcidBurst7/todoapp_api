FROM python:3.12.0

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]