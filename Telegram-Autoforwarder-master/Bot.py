import asyncio
from telethon import TelegramClient, events
import values as val

# Replace these with your own values
api_id = val.api_id
api_hash = val.api_hash
phone_number = val.phone_number

# Channel and Group IDs (use negative values for channel/group IDs)
source_channel_id = val.source_channel_id # Replace with your source channel ID
destination_group_id = val.destination_group_id # Replace with your destination group ID

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone_number)

    # Define the event handler for new messages in the source channel
    @client.on(events.NewMessage(chats=source_channel_id))
    async def handler(event):
        # Forward the received message to the destination group
        await client.send_message(destination_group_id, event.message)

        print(f"Message forwarded: {event.message.text}")

    # Keep the client running to listen for new messages
    print("Listening for new messages...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
