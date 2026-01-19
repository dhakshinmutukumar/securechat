"""
Streamlit dialog components for managing relations and group members.

This module contains UI dialogs for:
- Deleting a friend
- Leaving a group
- Adding members to a group
- Listing group members

All dialogs interact with repository-layer abstractions and update
Streamlit session state accordingly.
"""

from src.controller.relations_controller import RemoveFriend
from src.controller.groupmembers_controller import (
    RemoveFromGroup,
    AddGroupMembers,
    ListGroupMembers,
    RemainingGroupUsers,
)

import streamlit as st
import time
import pandas as pd

# ---------------------------------------------------------------------
# Repository Instances
# ---------------------------------------------------------------------
remove_friend = RemoveFriend()
remove_from_group = RemoveFromGroup()
add_group_members = AddGroupMembers()
list_group_members = ListGroupMembers()
remaining_group_users = RemainingGroupUsers()


# ---------------------------------------------------------------------
# Dialogs
# ---------------------------------------------------------------------


@st.dialog("Confirmation on delete")
def confirmdelete(name: str) -> None:
    """
    Confirm deletion of a friend.

    Args:
        item (str): Identifier of the friend to be removed.
    """
    st.write(f"Do you want to delete {name} from your Friends?")
    left, space, right = st.columns([1.2, 2, 1.2])

    with left:

        if st.button("Submit", icon=":material/check_circle:"):

            st.session_state.chat_with = None
            remove_friend(name)

    with right:

        if st.button("Cancel", icon=":material/cancel:"):
            st.rerun()


@st.dialog("Confirmation on Left")
def confirmleft(grpname: str, id: int) -> None:
    """
    Confirm leaving a group.

    Args:
        group_name (str): Name of the group.
        member_id (str): Identifier of the group membership entry.
    """
    st.write(f"Do you want to left from the group {grpname} ?")
    left, space, right = st.columns([1.2, 2, 1.2])

    with left:

        if st.button("Yes", icon=":material/check:"):

            st.session_state.chat_with = None
            remove_from_group(id)

    with right:

        if st.button("No", icon=":material/close:"):
            st.rerun()


@st.dialog("Add members to group")
def addmembers(grpid: int, name: str) -> None:
    """
    Add members to an existing group.

    Args:
        group_id (str): Group identifier.
        group_name (str): Group display name.
    """
    options = st.multiselect(
        f"Add members to {name}",
        remaining_group_users(grpid),
        placeholder="Choose users here",
    )

    with st.container(horizontal=True):

        with st.container(horizontal_alignment="left"):

            if st.button("Add", icon=":material/add:"):

                if len(options) == 0:
                    st.warning(
                        f"Choose atleast one member to add to {name}", width="stretch"
                    )

                else:
                    st.success(f"Added {options} in {name} group")
                    time.sleep(3)
                    add_group_members(members=options, grpid=grpid)
                    st.rerun()

        if st.button("Cancel", icon=":material/cancel:"):
            st.rerun()


@st.dialog("Group Members")
def listmembers(id: int, grpname: str) -> None:
    """
    Display all members of a group.

    Args:
        group_id (int): Group identifier.
        group_name (str): Group display name.
    """
    st.write(f"Members of the group {grpname}")
    df = pd.DataFrame({"members": list_group_members(id)})
    st.dataframe(df, hide_index=True)
