import sqlite3
from typing import Iterable

from db.repositories import repository
from db.connection import connection
from domain.messages import GroupMessage


class groupmessagerepo(repository):

    def add(self, sender: str, grpid: int, msg: str) -> None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "INSERT INTO grpmessages (grpid, sender, message) VALUES (?, ?, ?)",
                (grpid, sender, msg),
            )

    def getall(self, groupid: int) -> Iterable[GroupMessage]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT sender, message FROM grpmessages WHERE grpid = ?",
                (groupid,),
            )
            for sender, message in c.fetchall():

                yield GroupMessage(
                    sender=sender,
                    group_id=groupid,
                    content=message,
                )
