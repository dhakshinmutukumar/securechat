from typing import Iterable
from db.directmessages_repo import directmessagesrepo
from domain.messages import DirectMessage

_repo = directmessagesrepo()


class SendDirectMessage:
    def __call__(self, sender: str, receiver: str, message: str) -> None:
        _repo.add(sender, receiver, message)


class FetchDirectMessages:
    def __call__(self, user1: str, user2: str) -> Iterable[DirectMessage]:
        return _repo.getall(user1, user2)
