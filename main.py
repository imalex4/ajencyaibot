import openai
import telebot


openai.api_key = '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'
bot = telebot.TeleBot("5901663425:AAEdMtjqSgLbZF649mD_uAW7O6Pl247Pi5Q")
start_flag = False

@bot.message_handler(func=lambda _: True)
def handle_message(message):
  global start_flag
  if message.text.startswith("/"):
    start_flag = True
    return
  if start_flag:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
  )
  bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])
start_flag = False

bot.polling()