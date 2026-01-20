import streamlit as st
from typing import Optional, Iterable
from src.db.repositories import repository, association, group
from src.db.groups_repo import groupsrepo
from src.db.connection import connection
from src.domain.group import Group
from typing import cast, Any

repo = groupsrepo()


class groupmembersrepo(repository, association, group):

    def remainingusers(self, grpid: int) -> list[str]:
        supabase = connection.get()

        response = supabase.table("users").select("username").execute()
        raw_users = cast(list[dict[str, Any]], response.data or [])

        members = set(self.listbyid(grpid))

        return [row["username"] for row in raw_users if row["username"] not in members]

    def add(
        self,
        members: list[str],
        name: Optional[str] = None,
        grpid: Optional[int] = None,
    ) -> None:
        supabase = connection.get()

        if grpid is None:
            if name is None:
                raise ValueError("Group name required when grpid is None")
            grpid = repo.add(name)

        supabase.table("groupmembers").insert(
            [{"grpid": grpid, "username": m} for m in members]
        ).execute()

    def getall(self) -> Iterable[Group]:
        supabase = connection.get()

        response = (
            supabase.table("groupmembers")
            .select("grpid, groups(name)")
            .eq("username", st.session_state.user)
            .execute()
        )

        for row in response.data:
            yield Group(id=row["grpid"], name=row["groups"]["name"])

    def deletebyid(self, grpid: int) -> None:
        supabase = connection.get()

        supabase.table("groupmembers").delete().match(
            {
                "grpid": grpid,
                "username": st.session_state.user,
            }
        ).execute()

    def listbyid(self, id: int) -> list[str]:
        supabase = connection.get()

        response = (
            supabase.table("groupmembers").select("username").eq("grpid", id).execute()
        )

        return [row["username"] for row in response.data]
