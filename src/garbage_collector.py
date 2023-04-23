import asyncio

from src import logging_config
from src.observer import Observer
from os import remove


class GarbageCollector(Observer):
    def __init__(self, priority: int):
        super().__init__(priority)

    async def update(self, filename: str):
        await self.delete_garbage(filename)

    async def delete_garbage(self, filename: str):
        await asyncio.to_thread(remove, filename)
        logging_config.logging.info(filename + " removed!")
