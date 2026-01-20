from typing import Iterable
from src.db.repositories import repository
from src.db.connection import connection
from src.domain.messages import DirectMessage


class directmessagesrepo(repository):

    def add(self, sender: str, receiver: str, message: str) -> None:
        supabase = connection.get()

        supabase.table("messages").insert({
            "sender": sender,
            "receiver": receiver,
            "message": message,
        }).execute()

    def getall(self, user1: str, user2: str) -> Iterable[DirectMessage]:
        supabase = connection.get()

        response = (
            supabase.table("messages")
            .select("sender, receiver, message")
            .or_(
                f"and(sender.eq.{user1},receiver.eq.{user2}),"
                f"and(sender.eq.{user2},receiver.eq.{user1})"
            )
            .order("created_at")
            .execute()
        )

        for row in response.data:
            yield DirectMessage(
                sender=row["sender"],
                receiver=row["receiver"],
                content=row["message"],
            )
