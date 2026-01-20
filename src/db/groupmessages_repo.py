from typing import Iterable
from src.db.repositories import repository
from src.db.connection import connection
from src.domain.messages import GroupMessage


class groupmessagerepo(repository):

    def add(self, sender: str, grpid: int, msg: str) -> None:
        supabase = connection.get()

        supabase.table("grpmessages").insert({
            "sender": sender,
            "grpid": grpid,
            "message": msg,
        }).execute()

    def getall(self, groupid: int) -> Iterable[GroupMessage]:
        supabase = connection.get()

        response = (
            supabase.table("grpmessages")
            .select("sender, message")
            .eq("grpid", groupid)
            .order("created_at")
            .execute()
        )

        for row in response.data:
            yield GroupMessage(
                sender=row["sender"],
                group_id=groupid,
                content=row["message"],
            )
