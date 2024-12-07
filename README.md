
# Telegram Chat Cleanup Bot

This Python script uses the **Telethon** library to automate the cleanup of unwanted conversations in your Telegram account. It supports the following features:
- Deletes chats with deleted accounts.
- Removes empty conversations.
- Cleans up chats containing specific messages like "joined Telegram!".

## Features
- **Delete Chats with Deleted Accounts:** Automatically detects and deletes conversations with users whose accounts are no longer active.
- **Remove Empty Conversations:** Deletes conversations that have no meaningful messages.
- **Filter Specific Messages:** Searches and deletes chats containing specific phrases like "joined Telegram!".

## Prerequisites
- Python 3.9+ installed on your system.
- **Termux** (optional): Use Termux on Android to run the script.
- A Telegram account with API credentials.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/telegram-chat-cleanup-bot.git
   cd telegram-chat-cleanup-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install telethon
   ```

3. Obtain your Telegram API credentials:
   - Go to [Telegram's API Development Tools](https://my.telegram.org/auth).
   - Log in with your Telegram account.
   - Create a new application and copy the **API ID** and **API Hash**.

## Usage
1. Edit the script `bot.py` and replace the following placeholders:
   ```python
   API_ID = 123456  # Replace with your API ID
   API_HASH = "your_api_hash"  # Replace with your API Hash
   ```

2. Run the script:
   ```bash
   python bot.py
   ```

3. Follow the prompts to log in and clean up your chats.

## Example Scripts
- **Delete Chats with Deleted Accounts**: Automatically cleans up conversations with users who have deleted their Telegram accounts.
- **Remove Empty Conversations**: Identifies and deletes conversations that are empty or only contain system messages.

## Notes
- **Privacy and Security**: Ensure you don’t share your API credentials or Telegram session files.
- Use this script responsibly. Do not violate Telegram's Terms of Service.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Pull requests are welcome. For significant changes, please open an issue first to discuss what you’d like to change.

## Acknowledgments
- [Telethon Documentation](https://docs.telethon.dev/)
- Telegram API Community
