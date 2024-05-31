

# Hafez Poetry Telegram Bot

This Telegram bot provides random Hafez poems along with their meanings when prompted with the `/fal` command. The bot is built using Python and the `python-telegram-bot` library, and it reads the poems from an XLSX file.

## Features

- Start the bot with `/start` to get a welcome message.
- Use `/fal` to receive a random Hafez poem and its meaning.

## Prerequisites

- Python 3.7+
- Telegram Bot API token
- An XLSX file containing Hafez poems and their meanings

## Setup

1. Clone the repository:

   
bash
   git clone https://github.com/Mohammadk202/test_bot
   cd hafez-poetry-bot
  

2. Install the required packages:

   
bash
   pip install -r requirements.txt
  

3. Place your `Faal.xlsx` file in the root directory of the project. Ensure the XLSX file has the following columns:
   - Column A: Poem
   - Column B: Meaning

4. Replace the placeholder with your actual Telegram Bot API token in `hafez_bot.py`:

   
python
   token = "YOUR_TELEGRAM_BOT_API_TOKEN"
  

## Running the Bot

1. Run the bot using the following command:

   
bash
   python hafez_bot.py
  

2. Open your Telegram app and start a chat with your bot. Use the `/start` command to initiate the conversation and then use `/fal` to receive a random Hafez poem.

## Deployment

To deploy the bot to a platform like Railway, follow these steps:

1. Create a new project on Railway and link it to your GitHub repository.
2. Set the environment variable `BOT_TOKEN` with your Telegram Bot API token in the Railway project settings.
3. Deploy the project, and Railway will automatically build and run the bot.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details
