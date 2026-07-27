import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from heandlers import register_routers


async def main() -> None:

    bot = Bot(BOT_TOKEN)

    dp = Dispatcher(
        storage=MemoryStorage()
    )

    register_routers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())