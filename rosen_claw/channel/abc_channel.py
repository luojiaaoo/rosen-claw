from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: str


@dataclass
class ToolResult:
    id: str
    name: str
    result: str
    is_error: bool = False


class ABCChannel(ABC):
    @abstractmethod
    async def receive_input(self, message: str) -> str:
        """用户输入"""
        ...

    @abstractmethod
    async def send_text_chunk(self, chunk: str) -> None:
        """流式文本回复片段"""
        ...

    @abstractmethod
    async def send_tool_call_chunk(self, chunk: ToolCall) -> None:
        """发送工具调用请求"""
        ...

    @abstractmethod
    async def send_tool_result_chunk(self, chunk: ToolResult) -> None:
        """发送工具执行结果"""
        ...

    @abstractmethod
    async def run(self) -> None:
        """启动频道主循环"""
        ...
