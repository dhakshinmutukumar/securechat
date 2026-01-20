from abc import ABC, abstractmethod
from typing import Any


class repository(ABC):

    @abstractmethod
    def add(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    def getall(self, *args: Any, **kwargs: Any) -> Any:
        pass


class group(ABC):

    @abstractmethod
    def listbyid(self, *args: Any, **kwargs: Any) -> Any:
        pass


class association(ABC):

    @abstractmethod
    def deletebyid(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    def remainingusers(self, *args: Any, **kwargs: Any) -> Any:
        pass
