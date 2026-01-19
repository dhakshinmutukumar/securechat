import sqlite3
import os
import streamlit as st
from types import TracebackType
from typing import Optional, Type, Literal
from src.utils.config import DB_NAME as db

DB_NAME = db


class connection:
    def __init__(self) -> None:
        self.conn: Optional[sqlite3.Connection] = None

    def __enter__(self) -> sqlite3.Connection:
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        return self.conn

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Literal[False] | None:

        if self.conn is None:
            return False

        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        self.conn.close()
        return False
