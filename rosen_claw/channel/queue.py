from asyncio import Queue
class QueueChannel:
    def __init__(self):
        self._queue = Queue()

    async def receive_input(self, message: str) -> str:
