import streamlit as st
from src.db.repositories import repository, association
from src.db.connection import connection


class relationsrepo(repository, association):

    def add(self, receiver: str) -> None:
        supabase = connection.get()

        supabase.table("relations").insert([
            {"sender": st.session_state.user, "receiver": receiver},
            {"sender": receiver, "receiver": st.session_state.user},
        ]).execute()

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

        supabase.table("relations").delete().match({
            "sender": st.session_state.user,
            "receiver": user,
        }).execute()

    def remainingusers(self) -> tuple[list[str], list[str]]:
        supabase = connection.get()

        users = supabase.table("users").select("username").execute().data
        friends = set(self.getall())

        friend_list, nonfriend_list = [], []

        for u in users:
            if u["username"] == st.session_state.user:
                continue
            if u["username"] in friends:
                friend_list.append(u["username"])
            else:
                nonfriend_list.append(u["username"])

        return friend_list, nonfriend_list
