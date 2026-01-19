import hashlib
import sqlite3

import streamlit as st
from src.db.repositories import repository
from src.db.connection import connection


class usersrepo(repository):

    def add(self, username: str, password: str, email: str) -> None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            pwd_hash: str = hashlib.sha256(password.encode()).hexdigest()
            c.execute(
                "INSERT INTO User (username, password_hash, email) VALUES (?, ?, ?)",
                (username, pwd_hash, email),
            )

    def getall(self) -> list[str]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT username FROM User WHERE username != ?",
                (st.session_state.user,),
            )
            users: list[str] = [row[0] for row in c.fetchall()]
            return users

    def user_exists(self, username: str) -> bool:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT username FROM User WHERE username = ?",
                (username,),
            )
            return c.fetchone() is not None

    def validate_user(self, username: str, password: str) -> bool:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT password_hash FROM User WHERE username = ? LIMIT 1",
                (username,),
            )
            row = c.fetchone()
            if row:
                pwd_hash: str = hashlib.sha256(password.encode()).hexdigest()
                return pwd_hash == row[0]
            return False

    def email_exists(self, email: str) -> bool:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT email FROM User WHERE email = ? LIMIT 1",
                (email,),
            )
            return c.fetchone() is not None
