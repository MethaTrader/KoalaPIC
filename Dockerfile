FROM python:3.9

WORKDIR app/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Запускаємо додаток
CMD ["python3", "./app/main.py"]