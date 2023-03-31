FROM python:3.9

ENV OPENAI_API_KEY ${OPENAI_API_KEY}
ENV BOT_TOKEN ${BOT_TOKEN}

WORKDIR app/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Запускаємо додаток
CMD ["uvicorn", "app.bot:app", "--host", "0.0.0.0", "--port", "80"]