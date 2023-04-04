FROM python:3.9

ENV OPENAI_API_KEY ${OPENAI_API_KEY}
ENV BOT_TOKEN ${BOT_TOKEN}

WORKDIR app/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Запускаємо додаток
CMD ["python", "app/bot.py"]