import os
import json

import streamlit as st


def banner():
    st.title("Pilot3 Leaderboard")


def load_competition_data():
    files = os.listdir("competition")

    if "competition_data.csv" not in files or "config.json" not in files:
        st.sidebar.text("Admin please add competition data.")
    else:
        test_data = pd.read_csv("competition/data.csv")
        with open("competition/config.json") as f:
            config = json.load(f)

        return data, config


