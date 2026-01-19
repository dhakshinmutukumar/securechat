import sqlite3
from typing import Iterable, Optional

import streamlit as st
from db.repositories import repository, association, group
from db.groups_repo import groupsrepo
from db.connection import connection
from domain.group import Group

repo: repository = groupsrepo()


class groupmembersrepo(repository, association, group):

    def remainingusers(self, grpid: int) -> list[str]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                """
                SELECT u.username
                FROM User u
                LEFT JOIN GroupMembers gm
                    ON u.username = gm.user
                    AND gm.grpid = ?
                WHERE gm.user IS NULL
                """,
                (grpid,),
            )
            nonusers: list[str] = [row[0] for row in c.fetchall()]
            return nonusers

    def add(
        self,
        members: list[str],
        name: Optional[str] = None,
        grpid: Optional[int] = None,
    ) -> None:

        with connection() as conn:
            if grpid is None:
                grpid = repo.add(name)

            c: sqlite3.Cursor = conn.cursor()
            rows: list[tuple[int, str]] = [(grpid, member) for member in members]
            c.executemany(
                "INSERT INTO groupmembers (grpid, user) VALUES (?, ?)",
                rows,
            )

    def getall(self) -> Iterable[Group]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                """
                SELECT g.grp_id, g.name
                FROM groups g
                JOIN groupmembers gm
                    ON g.grp_id = gm.grpid
                WHERE gm.user = ?
                """,
                (st.session_state.user,),
            )

            for gid, name in c.fetchall():
                yield Group(id=gid, name=name)

    def deletebyid(self, grpid: int) -> None:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "DELETE FROM groupmembers WHERE grpid = ? AND user = ?",
                (grpid, st.session_state.user),
            )

    def listbyid(self, id: int) -> list[str]:
        with connection() as conn:
            c: sqlite3.Cursor = conn.cursor()
            c.execute(
                "SELECT user FROM groupmembers WHERE grpid = ?",
                (id,),
            )
            members: list[str] = [row[0] for row in c.fetchall()]
            return members
