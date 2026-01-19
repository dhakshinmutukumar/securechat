import sqlite3

import streamlit as st
from db.repositories import repository
from db.connection import connection


class groupsrepo(repository):

    def add(self, name: str) -> int | None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "INSERT INTO groups (name) VALUES (?)",
                (name,),
            )
            group_id: int | None = c.lastrowid
            return group_id

    def getall(self, grpid: list[int]) -> list[str]:
        if not grpid:
            return []

        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            placeholders: str = ",".join("?" * len(grpid))
            query: str = f"SELECT name FROM groups WHERE grp_id IN ({placeholders})"
            c.execute(query, grpid)
            groups: list[str] = [row[0] for row in c.fetchall()]
            return groups
