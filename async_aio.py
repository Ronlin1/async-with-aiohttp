import aiohttp
import asyncio
from timeit import default_timer
from aiohttp import ClientSession
import warnings
warnings.filterwarnings("ignore")

urls = ['https://nytimes.com',
            'https://github.com',
            'https://google.com',
            'https://reddit.com',
            'https://hashnode.com',
            'https://producthunt.com']

async def fetch_status():
    start_time = default_timer()
    
    async with ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                print(f"[+] Getting Link [+] {url}  === {response.status} ")
    
    time_elapsed = default_timer() - start_time
    print("It took --- {} seconds --- for all the links"
      .format(time_elapsed))
    

async def main():
        await fetch_status()
                
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

