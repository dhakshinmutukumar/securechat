"""
Application entry point and page orchestrator for the Streamlit Chat App.

Responsibilities:
- Initialize Streamlit session state
- Route between login, signup, and chat screens
"""

from typing import Any

import streamlit as st

from src.screens import login_screen
from src.screens import signup_screen
from src.screens import chat_screen

# ---------------------------------------------------------------------
# Session State Defaults
# ---------------------------------------------------------------------

DEFAULT_SESSION_STATE: dict[str, Any] = {
    "chat_with": None,
    "grpid": None,
    "page": "login",
    "user": "",
    "otpstatus": "",
    "otp": None,
    "chat": None,
    "signin": "Generate otp",
    "click": 0,
    "select": 0,
}


def initialize_session_state() -> None:
    """
    Initialize Streamlit session state with default values.

    Existing session values are preserved.
    """
    for key, value in DEFAULT_SESSION_STATE.items():
        st.session_state.setdefault(key, value)


def route_page() -> None:
    """
    Route the application to the appropriate screen
    based on the current page stored in session state.
    """
    page: str = st.session_state.page

    if page == "login":
        login_screen.login()

    elif page == "signup":
        signup_screen.signup()

    elif page == "chat":
        chat_screen.chatscreen()

    else:
        st.error("Invalid page state")


def main() -> None:
    """
    Main application workflow.
    """
    initialize_session_state()
    route_page()


if __name__ == "__main__":
    main()
