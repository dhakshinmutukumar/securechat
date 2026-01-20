from typing import cast, Any
from src.db.repositories import repository
from src.db.connection import connection



class groupsrepo(repository):

    def add(self, name: str) -> int | None:
        supabase = connection.get()

        response = (
            supabase.table("groups")
            .insert(
                {
                    "name": name,
                }
            )
            .execute()
        )

        data = cast(list[dict[str, Any]], response.data or [])

        if not data:
            return None

        return int(data[0]["grp_id"])

    def getall(self, grpid: list[int]) -> list[str]:
        if not grpid:
            return []

        supabase = connection.get()

        response = (
            supabase.table("groups").select("name").in_("grp_id", grpid).execute()
        )

        return [row["name"] for row in response.data]
