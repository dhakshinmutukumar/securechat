from abc import ABC, abstractmethod


class repository(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def getall(self):
        pass


class group(ABC):

    @abstractmethod
    def listbyid(self):
        pass


class association(ABC):

    @abstractmethod
    def deletebyid(self):
        pass

    @abstractmethod
    def remainingusers(self):
        pass
