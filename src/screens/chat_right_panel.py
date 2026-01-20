from typing import Iterable
import streamlit as st
from src.controller.groupmessages_controller import SendGroupMessage, FetchGroupMessages
from src.controller.directmessages_controller import (
    SendDirectMessage,
    FetchDirectMessages,
)
from src.domain.messages import DirectMessage, GroupMessage

send_direct = SendDirectMessage()
fetch_direct = FetchDirectMessages()

send_group = SendGroupMessage()
fetch_group = FetchGroupMessages()


def chatscreenright(current_user: str) -> None:

    chat_user = st.session_state.chat_with
    scene = st.session_state.chat
    messages: Iterable[DirectMessage] | Iterable[GroupMessage]

    if scene == "Direct":
        st.write(f"### Chat with **{chat_user}**")
        messages = fetch_direct(current_user, chat_user)

    elif scene == "groups":
        st.write(f"### Chat in **{chat_user}** Group")
        messages = fetch_group(st.session_state.grpid)

    st.markdown("---")
    icon = """ <svg xmlns="http://www.w3.org/2000/svg" height="15px" viewBox="0 -960 960 960" width="16px" fill="#e3e3e3"><path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z"/></svg>"""
    button = f""" <button style = "background-color: transparent ; border :none;">{icon}</button> """
    chat_box = st.container()

    with chat_box:

        if st.session_state.chat == "Direct":

            for msg in messages:

                with st.container(horizontal=True):

                    if msg.sender == current_user:
                        st.markdown(
                            f"""<p style='text-align:right; color:blue;'><b>You:</b> {msg.content}{button}</p>""",
                            unsafe_allow_html=True,
                        )

                    else:
                        st.markdown(
                            f"<p style='text-align:left; color:green;'><b>{msg.sender}:</b> {msg.content}</p>",
                            unsafe_allow_html=True,
                        )

        if st.session_state.chat == "groups":

            for msg in messages:

                with st.container(horizontal=True):

                    if msg.sender == current_user:
                        st.markdown(
                            f"<p style='text-align:right;color:blue;'><b>You:</b>{msg.content}{button}</p>",
                            unsafe_allow_html=True,
                        )

                    else:
                        st.markdown(
                            f"<p style='text-align:left; color:green;'><b>{msg.sender}:</b> {msg.content}</p>",
                            unsafe_allow_html=True,
                        )

        new_msg = st.chat_input("Type a message...")

        if new_msg:

            if st.session_state.chat == "Direct":
                send_direct(current_user, chat_user, new_msg)

            elif st.session_state.chat == "groups":
                send_group(current_user, st.session_state.grpid, new_msg)

            st.rerun()
