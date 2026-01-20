import bcrypt
import streamlit as st
from src.db.repositories import repository
from src.db.connection import connection


class usersrepo(repository):

    def add(self, username: str, password: str, email: str) -> None:
        supabase = connection.get()

        pwd_hash = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt(),
        ).decode()

        supabase.table("users").insert({
            "username": username,
            "password_hash": pwd_hash,
            "email": email,
        }).execute()

    def getall(self) -> list[str]:
        supabase = connection.get()

        response = (
            supabase.table("users")
            .select("username")
            .neq("username", st.session_state.user)
            .execute()
        )

        return [row["username"] for row in response.data]

    def user_exists(self, username: str) -> bool:
        supabase = connection.get()

        response = (
            supabase.table("users")
            .select("username")
            .eq("username", username)
            .limit(1)
            .execute()
        )

        return len(response.data) > 0

    def validate_user(self, username: str, password: str) -> bool:
        supabase = connection.get()

        response = (
            supabase.table("users")
            .select("password_hash")
            .eq("username", username)
            .limit(1)
            .execute()
        )

        if not response.data:
            return False

        stored_hash = response.data[0]["password_hash"]
        return bcrypt.checkpw(password.encode(), stored_hash.encode())

    def email_exists(self, email: str) -> bool:
        supabase = connection.get()

        response = (
            supabase.table("users")
            .select("email")
            .eq("email", email)
            .limit(1)
            .execute()
        )

        return len(response.data) > 0
