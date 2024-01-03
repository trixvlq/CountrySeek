import aiohttp
import httpx

async def get_country(name: str):
    url = f'https://restcountries.com/v3.1/name/{name}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data


async def get_country_weather(capital: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={capital}&appid=cb8801fceffebeb18636363fc0e20105&units=metric'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
