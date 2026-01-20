from supabase import create_client, Client
from typing import Final

from src.utils.config import SUPABASE_URL, SUPABASE_KEY


class connection:
    _client: Client | None = None

    @classmethod
    def get(cls) -> Client:
        if cls._client is None:
            cls._client = create_client(
                SUPABASE_URL,
                SUPABASE_KEY,
            )
        return cls._client
