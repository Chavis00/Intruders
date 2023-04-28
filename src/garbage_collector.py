import asyncio
import datetime

from src import logging_config
from src.observer import Observer
from os import remove


class GarbageCollector(Observer):
    def __init__(self, priority: int):
        super().__init__(priority)

    async def update(self, file_path: str, current_time=datetime.datetime) -> None:
        await self.delete_garbage(filename=file_path)

    async def delete_garbage(self, filename: str) -> None:
        await asyncio.to_thread(remove, filename)
        logging_config.logging.info(filename + " removed!")
