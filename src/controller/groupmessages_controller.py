from typing import Iterable
from db.groupmessages_repo import groupmessagerepo
from domain.messages import GroupMessage

_repo = groupmessagerepo()


class SendGroupMessage:
    def __call__(self, sender: str, grpid: int, message: str) -> None:
        _repo.add(sender, grpid, message)


class FetchGroupMessages:
    def __call__(self, grpid: int) -> Iterable[GroupMessage]:
        return _repo.getall(grpid)
