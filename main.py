# 使用 python3 main.py yourtoken 来启动，比如 python3 main.py 114514:ABCDEFGO_HIJKLMNOxE
import telebot
import sys
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
        bot.send_message(TARGET_CHANNEL, conditional_execution(message_text), "HTML")

    except:
        bot.reply_to(message, f"坏了，你发送的这条消息没法被清理。")


def conditional_execution(message_text: str):
    if "https://x.com" in message_text or "https://twitter.com" in message_text:
        return clean_twitter(message_text)
    elif "https://b23.tv" in message_text or "https://bilibili.com" in message_text:
        return clean_bilibili(message_text)


def clean_twitter(message_text):
    if "?" in message_text:
        first_question_mark_index = message_text.find("?")
        if first_question_mark_index != -1:
            message_text = message_text[:first_question_mark_index]

    cleaned_link = message_text.replace("https://x.com", "https://fxtwitter.com")
    cleaned_link = cleaned_link.replace("https://twitter.com", "https://fxtwitter.com")

    return cleaned_link


def clean_bilibili(message_text):
    if "https://b23.tv" in message_text:
        message_text = re.findall(r"https://\S+", message_text)[-1]
        target_url = requests.get(message_text, allow_redirects=False).text
        return re.search(r'<a href="(.*?)\?', target_url).group(1)

    elif (
        "https://bilibili.com" in message_text
        or "https://www.bilibili.com" in message_text
    ):
        if "?" in message_text:
            return message_text.split("?")[0]
        else:
            return message_text

    else:
        return message_text


if __name__ == "__main__":
    bot.infinity_polling()
