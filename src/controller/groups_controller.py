from db.groups_repo import groupsrepo

_repo = groupsrepo()


class CreateGroup:
    def __call__(self, name: str) -> int:
        return _repo.add(name)


class FetchGroups:
    def __call__(self, grpids: list[int]) -> list[str]:
        return _repo.getall(grpids)
