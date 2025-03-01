import telebot
from lectai import LectAI  # Import your custom library

# Initialize Telegram bot
TOKEN = "5866712065:AAGmj5tnealwuEkvgojXC-MpGF7DeHqMGB0"
bot = telebot.TeleBot(TOKEN)

# Initialize LectAI client
client = LectAI()

# Start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a message and I'll respond using LectAI.")

# Handle messages
@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = client.get_response(message.text)  # Call LectAI API
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

# Run the bot
if __name__ == "__main__":
    bot.polling()
