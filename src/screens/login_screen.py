import streamlit as st
from utils.validtions_utils import is_valid_email
from controller.users_controller import UserExists, ValidateUser


def login() -> None:

    user_exists = UserExists()
    validate_user = ValidateUser()

    st.title("🏠 Chat App - Login")

    st.set_page_config(initial_sidebar_state="collapsed")

    user_id = st.text_input("Enter User ID")

    password = st.text_input("Enter password")

    left_col, spaces, right_col = st.columns([1.2, 5, 1.3])  # equal width

    with left_col:
        loginb = st.button("Login", icon=":material/login:")

    with right_col:
        signupb = st.button("Sign-up", icon=":material/start:")

    if loginb:

        if not user_id:
            st.warning("Enter user-id")

        elif not user_exists(user_id):

            if not is_valid_email(user_id):
                st.error("User not found. Enter correct user-id")
            else:
                st.error("user not found")

        elif not password:
            st.warning("Enter password")

        elif not validate_user(user_id, password):
            st.error("Enter correct password")

        else:
            st.session_state.user = user_id
            st.session_state.page = "chat"
            st.success("Login - successfull")
            st.rerun()

    elif signupb:
        st.session_state.page = "signup"
        st.rerun()
