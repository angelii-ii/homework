import adiyogi_weather
from adiyogi_weather import Adiyogi
import asyncio

async def main(latnum, lonnum):
    async with Adiyogi() as client:
        # Get current weather
        weather = await client.weather.get_current(
            lat=latnum,
            lon=lonnum
        )
        
        print(f"Temperature: {weather.temperature}°C")
        print(f"Condition: {weather.condition}")

if __name__ == "__main__":
    latnum = input("enter latitude\n")
    lonnum= input("enter longitude\n")
    asyncio.run(main(latnum, lonnum))