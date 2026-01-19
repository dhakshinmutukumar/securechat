from typing import Protocol, Iterable, Any


class Command(Protocol):
    def __call__(self, *args, **kwargs) -> None: ...


class Query(Protocol):
    def __call__(self, *args, **kwargs) -> Iterable[Any]: ...
