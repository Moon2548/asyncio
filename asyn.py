import asyncio
import aiohttp
import time

URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_all():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        return results
