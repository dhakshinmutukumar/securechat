import sqlite3
from typing import Iterable

from db.repositories import repository
from db.connection import connection
from domain.messages import DirectMessage


class directmessagesrepo(repository):

    def add(self, sender: str, receiver: str, message: str) -> None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                """
                INSERT INTO Message (sender, receiver, message)
                VALUES (?, ?, ?)
                """,
                (sender, receiver, message),
            )

    def getall(self, user1: str, user2: str) -> Iterable[DirectMessage]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                """
                SELECT sender, receiver, message
                FROM Message
                WHERE
                    (sender = ? AND receiver = ?)
                     OR
                    (sender = ? AND receiver = ?)
                ORDER BY message_id ASC
                """,
                (user1, user2, user2, user1),
            )
            for sender, receiver, message in c.fetchall():

                yield DirectMessage(sender=sender, receiver=receiver, content=message)
