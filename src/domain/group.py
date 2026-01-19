from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Group:
    id: int
    name: str
