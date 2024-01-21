import asyncio

async def print_numbers():
    for i in range(5):
        await asyncio.sleep(1)
        print(i)

async def print_letters():
    for letter in 'ABCDE':
        await asyncio.sleep(1)
        print(letter)

# Create an event loop
loop = asyncio.get_event_loop()

# Schedule the tasks in the event loop
tasks = [print_numbers, print_letters]