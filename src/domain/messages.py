from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DirectMessage:
    sender: str
    receiver: str
    content: str


@dataclass(frozen=True, slots=True)
class GroupMessage:
    sender: str
    group_id: int
    content: str
