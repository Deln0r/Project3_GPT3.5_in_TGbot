import os
import openai
import telebot

openai.api_key = os.getenv("")
bot = telebot.TeleBot('')

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt = message.text,
        messages=[],
        temperature=0.5,
        max_tokens=1000
    )
    bot.send_message(chat_id=message.from_user.id, text = response['choices'][0]['text'])

bot.polling()

1