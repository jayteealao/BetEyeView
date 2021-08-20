import os
import asyncio
check = os.environ.get('AWS_REGION', None)

if check == None:
    import sys
    sys.path.append("C:/Users/HP/Documents/dev/BetEyeView")
print(sys.path)


from populate.crud.create import populate_tables
from populate.database import database, engine, metadata
from populate.utils.logger import get_logger

logger = get_logger(__name__)


async def main():
    try:
        await database.connect()
        logger.info('Database connection established')
    except Exception as e:
        logger.error(e)
    async with database.transaction():
        try:
            await populate_tables()
            logger.info('Tables populated')
        except Exception as e:
            logger.error(e)


def handler(event, context):
    logger.info('Started function')
    asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())

