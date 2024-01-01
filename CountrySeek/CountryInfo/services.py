import aiohttp


async def get_country(name: str):
    url = f'https://restcountries.com/v3.1/name/{name}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data