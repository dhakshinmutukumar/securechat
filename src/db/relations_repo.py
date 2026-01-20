from typing import cast, Any
import streamlit as st
from src.db.repositories import repository, association
from src.db.connection import connection



class relationsrepo(repository, association):

    def add(self, receiver: str) -> None:
        supabase = connection.get()

        supabase.table("relations").upsert(
            [
                {"sender": st.session_state.user, "receiver": receiver},
                {"sender": receiver, "receiver": st.session_state.user},
            ],
            on_conflict="sender,receiver",
        ).execute()

    def getall(self) -> list[str]:
        supabase = connection.get()

        response = (
            supabase.table("relations")
            .select("receiver")
            .eq("sender", st.session_state.user)
            .execute()
        )

        return [row["receiver"] for row in response.data]

    def deletebyid(self, user: str) -> None:
        supabase = connection.get()

        supabase.table("relations").delete().match(
            {
                "sender": st.session_state.user,
                "receiver": user,
            }
        ).execute()

    def remainingusers(self) -> tuple[list[str], list[str]]:
        supabase = connection.get()

        response = supabase.table("users").select("username").execute()
        raw_data = response.data or []

        users = cast(list[dict[str, Any]], raw_data)

        friends = set(self.getall())

        friend_list: list[str] = []
        nonfriend_list: list[str] = []

        for row in users:
            username = row["username"]

            if username == st.session_state.user:
                continue

            if username in friends:
                friend_list.append(username)
            else:
                nonfriend_list.append(username)

        return friend_list, nonfriend_list
