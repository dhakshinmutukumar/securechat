"""
Utility functions for email validation and OTP delivery.

This module handles:
- Email format validation
- OTP generation
- Secure email delivery using SMTP
"""

import re
import random
import ssl
import smtplib
import time
import os

from email.message import EmailMessage
from utils.config import SENDER_EMAIL as senderemail
from utils.config import SENDER_PASSWORD as password

import streamlit as st


@st.cache_data(max_entries=15)
def is_valid_email(email: str) -> bool:
    """
    Validate email format using a regular expression.
    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if email format is valid, False otherwise.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def sendotp(email: str) -> None:
    """
    Generate and send a one-time password (OTP) to the given email address.

    The OTP is stored in Streamlit session state for later verification.

    Args:
        email (str): Recipient email address.
    """
    try:
        with st.status("Sending OTP...", expanded=False) as status:

            st.text("sending mail...")
            SMTP_SERVER = "smtp.gmail.com"
            SMTP_PORT = 465
            SENDER_EMAIL = senderemail

            SENDER_PASSWORD = password

            otp = random.randint(100000, 999999)
            st.session_state.otp = str(otp).strip()

            if SENDER_EMAIL is None or SENDER_PASSWORD is None:
                raise RuntimeError("Email credentials not configured")

            msg = EmailMessage()
            msg["Subject"] = "Your OTP Code for ChatApp"
            msg["From"] = SENDER_EMAIL
            msg["To"] = email
            msg.set_content(f"Your OTP is: {otp}")

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)

        status.update(label="OTP sent to your email!", state="complete", expanded=False)
        time.sleep(2)

    except Exception:
        st.error("Try in you own network")
        time.sleep(2)
