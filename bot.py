import requests
from bs4 import BeautifulSoup
import telegram
import asyncio

# Telegram bot token and chat ID
bot_token = '6723210705:AAEGB7EVE0TAVhmPl4Hntv8vY6lRXjFJ1go'
chat_id = '@webb0t'

# Send a GET request to the website
url = 'https://www.ethiopia-insight.com/category/newsanalysis/'
response = requests.get(url)

s = BeautifulSoup(response.text, 'html.parser')
posts = s.find_all('article')

# Create a Telegram bot instance
bot = telegram.Bot(token=bot_token)

async def send_message_async(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

async def main():
    for post in posts:
        title = post.find('h2', class_='entry-title').text
        image_element = post.find('img')
        image = image_element['src'] if image_element else ''
        date = post.find('span', class_='updated').text

        # Check if the <p> element exists before accessing its text attribute
        content_element = post.find('p')
        content = content_element.text if content_element else 'No content available.'

        # Construct the message to send
        message = f"Title: {title}\nDate: {date}\nImage: {image}\nContent: {content}"

        # Send the message to the Telegram channel
        await send_message_async(chat_id, message)

# Run the main function using asyncio.run()
asyncio.run(main())