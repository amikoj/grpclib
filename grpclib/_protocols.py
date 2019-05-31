from typing import Mapping, Any
from typing_extensions import Protocol

from . import const
from . import server
from . import events


class IServable(Protocol):
    def __mapping__(self) -> Mapping[str, const.Handler]: ...


class IClosable(Protocol):
    def close(self) -> None: ...


class IProtoMessage(Protocol):
    @classmethod
    def FromString(cls, s: bytes) -> 'IProtoMessage': ...

    def SerializeToString(self) -> bytes: ...


class IEventsTarget(Protocol):
    __dispatch__: 'events._Dispatch'


class IServerMethodFunc(Protocol):
    async def __call__(self, stream: 'server.Stream[Any, Any]') -> None: ...
