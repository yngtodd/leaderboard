import os

import streamlit as st


def banner():
    st.title("Pilot3 Leaderboard")


def load_competition_data():
    files = os.listdir("competition")

