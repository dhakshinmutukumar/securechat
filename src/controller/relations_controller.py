from db.relations_repo import relationsrepo

_repo = relationsrepo()


class AddFriend:
    def __call__(self, username: str) -> None:
        _repo.add(username)


class ListFriends:
    def __call__(self) -> list[str]:
        return _repo.getall()


class RemoveFriend:
    def __call__(self, username: str) -> None:
        _repo.deletebyid(username)


class RemainingUsers:
    def __call__(self) -> tuple[list[str], list[str]]:
        return _repo.remainingusers()
