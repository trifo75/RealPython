# site_checker_v0.py

import aiohttp
import asyncio

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"{url}: type -> {html[:20].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://google.com"),
        check("https://facebook.com"),
        check("https://netrisk.hu"),
        check("https://spar.hu"),
    )

asyncio.run(main())

# namost ez _valamiért_ elhasal azzal, hogy "RuntimeError: Event loop is closed"
# a legutolsóként válaszoló URL text részét nem tudja már lekérdezni. 


