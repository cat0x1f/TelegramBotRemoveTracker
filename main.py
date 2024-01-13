# 使用 python3 main.py yourtoken 来启动，比如 python3 main.py 114514:ABCDEFGO_HIJKLMNOxE
import telebot
import sys
from urllib.parse import urlparse
import re
import requests

USER = ["@cat0x1f"]  # 只接收指定用户的消息
TARGET_CHANNEL = "@catweb31"  # 发送到这个频道
BOT_TOKEN = sys.argv[1]

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="MARKDOWN")


@bot.message_handler(func=lambda m: True)
def receive_url(message):
    try:
        message_text = message.text
        if "https://x.com" in message_text or "https://twitter.com" in message_text:
            bot.send_message(TARGET_CHANNEL, clean_twitter(message_text), "HTML")
        elif "https://b23.tv" in message_text or "https://bilibili.com" in message_text:
            print(clean_bilibili(message_text))
            bot.send_message(TARGET_CHANNEL, clean_bilibili(message_text), "HTML")

    except:
        bot.reply_to(message, f"坏了，你发送的这条消息没法被清理。")


def clean_twitter(message_text):
    """
    从`https://x.com/elonmusk/status/1744554956667904127?s=61`
    清理成`https://fxtwitter.com/elonmusk/status/1744554956667904127`"""

    parsed_url = urlparse(message_text)
    cleaned_domain = "fxtwitter.com"
    status_id_path = parsed_url.path
    cleaned_link = f"https://{cleaned_domain}{status_id_path}"
    return cleaned_link


def clean_bilibili(message_text):
    """从`https://b23.tv/cKGneGN`
    清理成`https://www.bilibili.com/video/BV1Hp4y1V7Wu/`"""

    if "https://b23.tv" in message_text:
        message_text = re.findall(r"https://\S+", message_text)[-1]
        target_url = requests.get(message_text, allow_redirects=False).text
        return re.search(r'<a href="(.*?)\?', target_url).group(1)
    elif (
        "https://bilibili.com" in message_text
        or "https://www.bilibili.com" in message_text
    ):
        return message_text.split("?")[0]
    elif "?" not in message_text:
        return message_text


bot.infinity_polling()
