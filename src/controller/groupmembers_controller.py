from typing import Iterable
from src.db.groupmembers_repo import groupmembersrepo
from src.domain.group import Group

_repo = groupmembersrepo()


class AddGroupMembers:
    def __call__(
        self, members: list[str], name: str | None = None, grpid: int | None = None
    ) -> None:

        _repo.add(members=members, name=name, grpid=grpid)


class ListUserGroups:
    def __call__(self) -> Iterable[Group]:
        return _repo.getall()


class RemoveFromGroup:
    def __call__(self, grpid: int) -> None:
        _repo.deletebyid(grpid)


class ListGroupMembers:
    def __call__(self, grpid: int) -> list[str]:
        return _repo.listbyid(grpid)


class RemainingGroupUsers:
    def __call__(self, grpid: int) -> list[str]:
        return _repo.remainingusers(grpid)
