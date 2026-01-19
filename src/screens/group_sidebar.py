import time
import streamlit as st
from utils.dialogs_utils import confirmleft, addmembers, listmembers
from controller.users_controller import ListUsers
from controller.groupmembers_controller import AddGroupMembers, ListUserGroups

list_users = ListUsers()
add_group_members = AddGroupMembers()
list_user_groups = ListUserGroups()


def groups() -> None:

    with st.container(horizontal=True):

        create_clicked = st.button(
            "Create group", icon=":material/add:", width="stretch"
        )
        select_clicked = st.button(
            "Select group", icon=":material/ink_selection:", width="stretch"
        )

    if create_clicked:
        st.session_state.click = 1
        st.session_state.select = 0
        st.rerun()

    if st.session_state.click == 1:
        options = st.multiselect(
            "Add members", list_users(), placeholder="Choose users here"
        )

        name = st.text_input("Enter group name")

        with st.container(horizontal=True):

            with st.container(horizontal_alignment="left"):

                if st.button("Create", width="content", icon=":material/create:"):

                    if len(options) == 0:
                        st.warning("Choose at least one person", width="stretch")

                    elif len(name) == 0:
                        st.warning("Group name cannot be empty")

                    else:
                        options.append(st.session_state.user)
                        add_group_members(members=options, name=name)
                        st.success("Group created!")
                        time.sleep(2)
                        st.session_state.click = 0
                        st.rerun()

            if st.button("Cancel", width="content", icon=":material/cancel:"):
                st.session_state.click = 0
                st.rerun()

    if select_clicked:
        st.session_state.click = 0
        st.session_state.select = 1
        st.rerun()

    if st.session_state.select == 1:

        with st.container(border=True):
            st.text("")
            st.write("### Groups")
            hasanygroup = False
            counter = 0
            grouplist = list_user_groups()

            for grp in grouplist:
                hasanygroup = True

                with st.container(horizontal=True):

                    if st.button(
                        "",
                        icon=":material/add_circle:",
                        key=f"{counter}-grp",
                        type="tertiary",
                        help="Add memebers",
                    ):
                        addmembers(grp.id, grp.name)

                    if st.button(
                        "",
                        icon=":material/group:",
                        key=f"{counter}",
                        type="tertiary",
                        help="See members",
                    ):
                        listmembers(grp.id, grp.name)

                    leftside, rightside = st.columns([7.5, 1])

                    with leftside:

                        if st.button(
                            f"{grp.name}",
                            use_container_width=True,
                            icon=":material/groups:",
                        ):
                            st.session_state.chat_with = grp.name
                            st.session_state.grpid = grp.id
                            st.rerun()

                    with rightside:

                        if st.button(
                            "",
                            icon=":material/delete:",
                            key=f"{grp.name}",
                            type="tertiary",
                        ):
                            confirmleft(grp.name, grp.id)

                counter += 1

            if not hasanygroup:
                st.info("You are not in any groups. Create a group to chat in groups")
