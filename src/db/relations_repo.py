import sqlite3

import streamlit as st
from src.db.repositories import repository, association
from src.db.connection import connection


class relationsrepo(repository, association):

    def add(self, receiver: str) -> None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "INSERT OR IGNORE INTO Relations (sender, receiver) VALUES (?, ?)",
                (st.session_state.user, receiver),
            )
            c.execute(
                "INSERT OR IGNORE INTO Relations (sender, receiver) VALUES (?, ?)",
                (receiver, st.session_state.user),
            )

    def getall(self) -> list[str]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT receiver FROM Relations WHERE sender = ?",
                (st.session_state.user,),
            )
            receivers: list[str] = [row[0] for row in c.fetchall()]
            return receivers

    def deletebyid(self, user: str) -> None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                """
                DELETE FROM Relations
                WHERE sender = ? AND receiver = ?
                """,
                (st.session_state.user, user),
            )

    def remainingusers(self) -> tuple[list[str], list[str]]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                """
                SELECT
                    u.username,
                    CASE
                        WHEN r.receiver IS NOT NULL THEN 'friend'
                        ELSE 'nonfriend'
                    END AS relation_type
                FROM User u
                LEFT JOIN Relations r
                    ON u.username = r.receiver
                    AND r.sender = ?
                WHERE u.username != ?
                """,
                (st.session_state.user, st.session_state.user),
            )

            friends: list[str] = []
            nonfriends: list[str] = []

            for username, relation in c.fetchall():
                if relation == "friend":
                    friends.append(username)
                else:
                    nonfriends.append(username)

            return friends, nonfriends
