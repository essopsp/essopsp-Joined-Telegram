from telethon import TelegramClient, types

# Replace these with your credentials
API_ID = ""  # Your API ID
API_HASH =""  # Your API Hash

# Create a new Telegram client session
client = TelegramClient('user_session', API_ID, API_HASH)

async def delete_empty_chats():
    print("Fetching chats...")
    async for dialog in client.iter_dialogs():
        # Check if the dialog is a User, and check if it contains any meaningful messages
        if isinstance(dialog.entity, types.User):
            empty = True
            # Iterate over all messages in the chat
            async for message in client.iter_messages(dialog.id):
                if message.text:  # If there's a message with text content
                    empty = False
                    break  # Stop checking once a meaningful message is found
            
            # If no meaningful message is found, delete the chat
            if empty:
                print(f"Deleting empty chat with: {dialog.name}")
                await client.delete_dialog(dialog.id)

    print("All empty conversations have been deleted!")

# Log in and run the script
with client:
    client.loop.run_until_complete(delete_empty_chats())
