import streamlit as st
from utils.dialogs_utils import confirmdelete
from controller.relations_controller import AddFriend

add_friend = AddFriend()


def directside(new_users: list[str], filtered: list[str]) -> None:

    query = st.selectbox("Search user", [""] + new_users)

    if query != "":

        if query not in filtered:
            add_friend(query)

    with st.container(border=True):
        st.text("")
        st.write("### Friends")

        if len(filtered) == 0:
            st.info("Select a user to chat")

        else:

            for user in filtered:

                with st.container():
                    leftside, rightside = st.columns([7.5, 1])

                    with leftside:

                        if st.button(
                            f"{user}",
                            use_container_width=True,
                            icon=":material/person:",
                        ):
                            st.session_state.chat_with = user
                            st.session_state.grpid = None
                            st.rerun()

                    with rightside:

                        if st.button(
                            "", icon=":material/delete:", key=f"{user}", type="tertiary"
                        ):
                            confirmdelete(user)
