import openai
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from mysql.connector import connect, Error

# set up OpenAI API credentials
openai.api_key = os.environ['OPENAI_API_KEY']
BOT_TOKEN = os.environ['BOT_TOKEN']
#BOT_TOKEN = 'my_secret_bot_token'
request_count = {}

def connect_db():
    try:
        with connect(
            host=os.environ['DB_HOST'],
            user="user",
            password="userpass",
            database="mydb",
        ) as connection:
            print(connection)
    except Error as e:
        print(e)
    finally:
        connection.close()

# define a function to generate an image based on user input
def generate_image(prompt):
    # use OpenAI's API to generate an image based on the user's prompt

    image_resp = openai.Image.create(prompt=prompt, n=1, size="512x512")
    generated_image_url = image_resp['data'][0]['url']
    return generated_image_url


async def start(update, context):
    user_id = update.effective_user.id
    try:
        with connect(
            host=os.environ['DB_HOST'],
            user="user",
            password="userpass",
            database="mydb",
        ) as connection:
            #select_query = "SELECT `id` FROM `account` WHERE `login` = `" + str(user_id) + "` "
            insert_query = "INSERT INTO `account` (login) VALUES (" + str(user_id) + ") "
            with connection.cursor() as cursor:
                cursor.execute(insert_query)
                connection.commit()
    except Error as e:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=e)
        print(e)
    finally:
        connection.close()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="🐨Привіт, я твоя Коала і зможу згенерувати для тебе круті зображення. Опиши своє майбутнє зображення та напиши мені, а я поки полазаю по деревам")


async def echo(update, context):
    user_id = update.effective_user.id
    if user_id in request_count and request_count[user_id] >= 10:
        update.message.reply_text("Вибачте, але ви дуже навантажуєте Коалу, спробуйте трохи пізніше.")
        return

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Зачекай, я генерую зображення...")

    try:
        # generate the image based on the user's message
        generated_image_url = generate_image(update.message.text)
        # send the generated image back to the user
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=generated_image_url)
        await context.bot.send_message(chat_id=update.message.chat_id,
                                       text="Якщо хочете ще зображень, просто пишіть мені нове повідомлення")
    except:
        await context.bot.send_message(chat_id=update.message.chat_id,
                                       text="Ви написали некорректний опис вашого зображення. Спробуйте ще раз.")
    finally:
        request_count[user_id] = request_count.get(user_id, 0) + 1


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    #connect_db()
    print("Bot started")

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
