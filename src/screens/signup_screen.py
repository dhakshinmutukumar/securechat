import time
from typing import ContextManager, Any
import streamlit as st
from controller.users_controller import CreateUser, UserExists, EmailExists
from utils.validtions_utils import is_valid_email, sendotp


create_user = CreateUser()
user_exists = UserExists()
email_exists = EmailExists()


def signup() -> None:

    st.title("🏠 Chat App - Signup")
    st.set_page_config(initial_sidebar_state="collapsed")
    field = st.container()
    localotp: str = ""
    with field:
        user_id = st.text_input("Enter User ID")
        password = st.text_input("Enter password")
        email = st.text_input("Enter e-mail ID")

        if st.session_state.otpstatus == "sent":
            localotp = st.text_input(" ## Enter the otp in the mail ##")

    left_col, spaces, right_col = st.columns([2.5, 7, 1.7])

    with left_col:
        signupb = st.button(st.session_state.signin, icon=":material/key:")

    with right_col:
        loginb = st.button("Login", icon=":material/login:")

        if loginb:
            st.session_state.page = "login"
            st.session_state.otpstatus = ""
            st.session_state.signin = "Generate otp"
            st.rerun()

    if signupb:

        if st.session_state.signin == "Generate otp":

            if not user_id:
                st.warning("Enter user-id")

            elif user_exists(user_id):
                st.error(
                    "user-id already exists. Go to login to continue (or) create any other user-id"
                )

            elif not password:
                st.warning("Enter password to sign-up")

            elif not email:
                st.warning("E-mail ID can't be null")

            elif not is_valid_email(email):
                st.warning("Enter valid e-mail id")

            elif email_exists(email):
                st.error("Email-ID already exist. Give any other mail ID")

            else:
                sendotp(email)
                st.success("OTP sent to your mail")
                st.session_state.otpstatus = "sent"
                st.session_state.signin = "Validate otp"
                st.rerun()

        elif st.session_state.signin == "Validate otp":
            statusexp(localotp, user_id, password, field, email)


def statusexp(
    localotp: str, user_id: str, password: str, field: ContextManager[Any], email: str
) -> None:

    with field:

        if localotp:

            if str(localotp).strip() == str(st.session_state.otp):
                create_user(user_id, password, email)
                st.success("User added successful.you will be re-directed to login")
                time.sleep(2)
                st.session_state.otp = None
                st.session_state.page = "login"
                st.rerun()

            elif localotp != "":
                st.error("enter otp correctly")

            else:
                st.warning("enter the otp first")
