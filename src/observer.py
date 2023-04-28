from abc import ABC, abstractmethod
import datetime


class Observer(ABC):
    def __init__(self, priority: int):
        self.priority = priority

    @abstractmethod
    def update(self, file_path: str, current_time: datetime.datetime):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    async def notify_observers(self, file_path: str):
        current_time = datetime.datetime.now()
        for observer in sorted(self.observers, key=lambda obs: obs.priority):
            await observer.update(file_path, current_time)
