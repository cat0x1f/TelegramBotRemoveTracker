FROM python:3.9-alpine

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pyTelegramBotAPI telebot

COPY . .

CMD python main.py $BOTTOKEN