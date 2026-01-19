import streamlit as st

from src.screens.chat_right_panel import chatscreenright
from src.screens.direct_sidebar import directside
from src.screens.group_sidebar import groups

from src.controller.relations_controller import RemainingUsers


def chatscreen() -> None:
    st.title("💬 Chat Screen")

    remaining_users = RemainingUsers()

    current_user = st.session_state.user

    filtered, new_users = remaining_users()

    with st.sidebar:

        st.markdown(f"## Welcome {st.session_state.user}")

        with st.container(horizontal=True):

            if st.button("Groups", width="stretch", icon=":material/groups:"):

                if st.session_state.chat == "Direct":
                    st.session_state.chat_with = None

                st.session_state.chat = "groups"
                st.rerun()

            if st.button("Direct", width="stretch", icon=":material/person:"):

                if st.session_state.chat == "groups":
                    st.session_state.chat_with = None

                st.session_state.chat = "Direct"
                st.session_state.click = 0
                st.session_state.select = 0
                st.rerun()

        if st.session_state.chat == "Direct":
            directside(new_users, filtered)

        elif st.session_state.chat == "groups":
            groups()

        if st.button(
            "Logout", use_container_width=True, type="primary", icon=":material/logout:"
        ):
            st.session_state.page = "login"
            st.session_state.user = ""
            st.session_state.click = 0
            st.session_state.select = 0
            st.session_state.chat_with = None
            st.session_state.chat = None
            st.rerun()

    with st.container(border=True):

        if st.session_state.chat_with is None:
            st.write("### Select a user or group from sidebar to start chatting")
            st.markdown("---")

        else:
            chatscreenright(current_user)
