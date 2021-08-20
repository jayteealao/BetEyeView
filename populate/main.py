from populate.crud.create import populate_tables
from populate.crud.read import read_by_league
from populate.database import database, engine, metadata
import asyncio


async def main():
    print('Initializing Scratch...')
    await database.connect()
    async with database.transaction():
        await populate_tables()
        test = await read_by_league("Premier League")
        for match in test:
            print(match)


def handler(event, context):
    asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())

